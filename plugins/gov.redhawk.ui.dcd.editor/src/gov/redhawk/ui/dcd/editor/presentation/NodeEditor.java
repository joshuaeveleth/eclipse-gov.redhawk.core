/**
 * This file is protected by Copyright. 
 * Please refer to the COPYRIGHT file distributed with this source distribution.
 * 
 * This file is part of REDHAWK IDE.
 * 
 * All rights reserved.  This program and the accompanying materials are made available under 
 * the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html.
 *
 */
package gov.redhawk.ui.dcd.editor.presentation;

import gov.redhawk.diagram.DiagramUtil;
import gov.redhawk.diagram.editor.URIEditorInputProxy;
import gov.redhawk.model.sca.ScaPackage;
import gov.redhawk.model.sca.util.ModelUtil;
import gov.redhawk.sca.dcd.diagram.DcdDiagramUtilHelper;
import gov.redhawk.sca.dcd.diagram.part.DcdDiagramEditor;
import gov.redhawk.sca.util.PluginUtil;
import gov.redhawk.ui.editor.SCAFormEditor;

import java.io.IOException;
import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import mil.jpeojtrs.sca.dcd.DcdPackage;
import mil.jpeojtrs.sca.dcd.DeviceConfiguration;
import mil.jpeojtrs.sca.dcd.provider.DcdItemProviderAdapterFactory;
import mil.jpeojtrs.sca.prf.provider.PrfItemProviderAdapterFactory;
import mil.jpeojtrs.sca.scd.provider.ScdItemProviderAdapterFactory;
import mil.jpeojtrs.sca.spd.provider.SpdItemProviderAdapterFactory;

import org.eclipse.core.resources.IMarker;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.command.BasicCommandStack;
import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.AdapterFactory;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.impl.AdapterImpl;
import org.eclipse.emf.common.ui.URIEditorInput;
import org.eclipse.emf.common.ui.viewer.IViewerProvider;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EValidator;
import org.eclipse.emf.ecore.provider.EcoreItemProviderAdapterFactory;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.edit.domain.AdapterFactoryEditingDomain;
import org.eclipse.emf.edit.provider.AdapterFactoryItemDelegator;
import org.eclipse.emf.edit.provider.ComposedAdapterFactory;
import org.eclipse.emf.edit.ui.provider.AdapterFactoryContentProvider;
import org.eclipse.emf.edit.ui.provider.AdapterFactoryLabelProvider;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.gef.EditPart;
import org.eclipse.gmf.runtime.diagram.ui.editparts.DiagramEditPart;
import org.eclipse.gmf.runtime.diagram.ui.editparts.IGraphicalEditPart;
import org.eclipse.gmf.runtime.diagram.ui.parts.IDiagramEditDomain;
import org.eclipse.gmf.runtime.diagram.ui.parts.IDiagramGraphicalViewer;
import org.eclipse.gmf.runtime.diagram.ui.parts.IDiagramWorkbenchPart;
import org.eclipse.gmf.runtime.diagram.ui.properties.views.PropertiesBrowserPage;
import org.eclipse.gmf.runtime.diagram.ui.resources.editor.ide.document.FileEditorInputProxy;
import org.eclipse.gmf.runtime.emf.core.util.EMFCoreUtil;
import org.eclipse.gmf.runtime.notation.Diagram;
import org.eclipse.jface.action.IMenuListener;
import org.eclipse.jface.action.IMenuManager;
import org.eclipse.jface.action.IStatusLineManager;
import org.eclipse.jface.action.IToolBarManager;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.ISelectionChangedListener;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.jface.viewers.SelectionChangedEvent;
import org.eclipse.jface.viewers.StructuredSelection;
import org.eclipse.jface.viewers.TreeViewer;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Label;
import org.eclipse.ui.IActionBars;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.editors.text.TextEditor;
import org.eclipse.ui.ide.IGotoMarker;
import org.eclipse.ui.part.MultiPageSelectionProvider;
import org.eclipse.ui.statushandlers.StatusManager;
import org.eclipse.ui.views.contentoutline.ContentOutlinePage;
import org.eclipse.ui.views.contentoutline.IContentOutlinePage;
import org.eclipse.ui.views.properties.IPropertySheetPage;
import org.eclipse.ui.views.properties.tabbed.ITabbedPropertySheetPageContributor;

/**
 * This is an example of a Dcd model editor.
 */
public class NodeEditor extends SCAFormEditor implements ITabbedPropertySheetPageContributor, IDiagramWorkbenchPart, IViewerProvider {

	public static final String ID = "gov.redhawk.ui.dcd.editor.presentation.NodeEditorID";

	public static final String EDITING_DOMAIN_ID = DcdDiagramEditor.EDITING_DOMAIN_ID;
	/**
	 * This is the content outline page.
	 */
	private IContentOutlinePage contentOutlinePage;

	/**
	 * This is a kludge...
	 */
	private IStatusLineManager contentOutlineStatusLineManager;

	/**
	 * This is the content outline page's viewer.
	 */
	private TreeViewer contentOutlineViewer;

	/**
	 * The graphical diagram editor embedded into this editor.
	 */
	private DcdDiagramEditor diagramEditor;

	/**
	 * This keeps track of the active content viewer, which may be either one of
	 * the viewers in the pages or the content outline viewer.
	 */
	private Viewer currentViewer;

	/**
	 * This selection provider coordinates the selections of the various editor
	 * parts.
	 */
	private final MultiPageSelectionProvider selectionProvider;

	private IEditorInput wrappedInput;

	private int dcdSourcePageNum;

	private final Adapter nameListener = new AdapterImpl() {
		/**
		 * {@inheritDoc}
		 */
		@Override
		public void notifyChanged(final Notification msg) {
			super.notifyChanged(msg);
			final int featureID = msg.getFeatureID(DeviceConfiguration.class);

			if (featureID == DcdPackage.DEVICE_CONFIGURATION__NAME) {
				if (msg.getEventType() == Notification.SET) {
					updateTitle();
				}
			}
		}
	};

	private final Adapter disposeListener = new AdapterImpl() {
		@Override
		public void notifyChanged(final org.eclipse.emf.common.notify.Notification msg) {
			switch (msg.getFeatureID(gov.redhawk.model.sca.IDisposable.class)) {
			case ScaPackage.IDISPOSABLE__DISPOSED:
				if (msg.getNewBooleanValue()) {
					PlatformUI.getWorkbench().getDisplay().asyncExec(new Runnable() {
						public void run() {
							getSite().getPage().closeEditor(NodeEditor.this, true);
						}
					});
				}
				break;
			default:
				break;
			}
		}
	};

	/**
	 * This creates a model editor.
	 */
	public NodeEditor() {
		super();
		initializeEditingDomain();
		this.selectionProvider = new MultiPageSelectionProvider(this);
		this.selectionProvider.addSelectionChangedListener(new ISelectionChangedListener() {
			public void selectionChanged(final SelectionChangedEvent event) {
				setStatusLineManager(event.getSelection());
			}
		});
	}

	/**
	 * This is here for the listener to be able to call it.
	 */
	@Override
	protected void firePropertyChange(final int action) {
		super.firePropertyChange(action);
	}

	/**
	 * Lazy initialization of the wrapped editor input.
	 * 
	 * @return
	 */
	protected IEditorInput getWrappedInput() {
		if (this.wrappedInput == null) {
			if (getEditorInput() instanceof IFileEditorInput) {
				this.wrappedInput = new FileEditorInputProxy((IFileEditorInput) getEditorInput(), (TransactionalEditingDomain) getEditingDomain());
			} else if (getEditorInput() instanceof URIEditorInput) {
				this.wrappedInput = new URIEditorInputProxy((URIEditorInput) getEditorInput(), (TransactionalEditingDomain) getEditingDomain());
			} else {
				// should not happen, but who knows...
				this.wrappedInput = getEditorInput();
			}
		}
		return this.wrappedInput;
	}

	/**
	 * This sets the selection into whichever viewer is active.
	 */
	@Override
	public void setSelectionToViewer(final Collection< ? > collection) {
		final Collection< ? > theSelection = collection;
		// Make sure it's okay.
		//
		if (theSelection != null && !theSelection.isEmpty()) {
			// I don't know if this should be run this deferred
			// because we might have to give the editor a chance to process the
			// viewer update events
			// and hence to update the views first.
			//
			//
			final Runnable runnable = new Runnable() {
				public void run() {
					// Try to select the items in the current content viewer of
					// the editor.
					//
					if (NodeEditor.this.currentViewer != null) {
						NodeEditor.this.currentViewer.setSelection(new StructuredSelection(theSelection.toArray()), true);
					}
				}
			};
			runnable.run();
		}
	}

	/**
	 * This makes sure that one content viewer, either for the current page or
	 * the outline view, if it has focus, is the current one.
	 */
	public void setCurrentViewer(final Viewer viewer) {
		// If it is changing...
		//
		if (this.currentViewer != viewer) {
			// Remember it.
			//
			this.currentViewer = viewer;
		}
	}

	/**
	 * This returns the viewer as required by the {@link IViewerProvider}
	 * interface.
	 */
	@Override
	public Viewer getViewer() {
		return this.currentViewer;
	}

	/**
	 * This is how the framework determines which interfaces we implement.
	 */
	@SuppressWarnings("rawtypes")
	@Override
	public Object getAdapter(final Class key) {
		if (key.equals(IPropertySheetPage.class)) {
			return getPropertySheetPage();
		} else if (key.equals(IGotoMarker.class)) {
			return this;
		} else if (key.equals(DeviceConfiguration.class)) {
			return PluginUtil.adapt(DeviceConfiguration.class, getDeviceConfiguration());
		} else {
			return super.getAdapter(key);
		}
	}

	/**
	 * This accesses a cached version of the property sheet.
	 */
	public IPropertySheetPage getPropertySheetPage() {
		return new PropertiesBrowserPage(this);
	}

	@Override
	public void gotoMarker(final IMarker marker) {
		try {
			if (marker.getType().equals(EValidator.MARKER)) {
				final String uriAttribute = marker.getAttribute(EValidator.URI_ATTRIBUTE, null);
				if (uriAttribute != null) {
					final URI uri = URI.createURI(uriAttribute);
					final EObject eObject = getEditingDomain().getResourceSet().getEObject(uri, true);
					if (eObject != null) {
						setSelectionToViewer(Collections.singleton(AdapterFactoryEditingDomain.getWrapper(eObject, getEditingDomain())));
					}
				}
			}
		} catch (final CoreException exception) {
			StatusManager.getManager().handle(new Status(IStatus.ERROR, NodeExplorerPlugin.getPluginId(), "Failed to go to marker.", exception),
			        StatusManager.LOG | StatusManager.SHOW);
		}
	}

	public void setStatusLineManager(final ISelection selection) {
		final IStatusLineManager statusLineManager;
		if (this.currentViewer != null && this.currentViewer == this.contentOutlineViewer) {
			statusLineManager = this.contentOutlineStatusLineManager;
		} else {
			statusLineManager = getActionBars().getStatusLineManager();
		}

		if (statusLineManager != null) {
			if (selection instanceof IStructuredSelection) {
				final Collection< ? > collection = ((IStructuredSelection) selection).toList();
				switch (collection.size()) {
				case 0:
					statusLineManager.setMessage("Selected Nothing");
					break;
				case 1:
					final String text = new AdapterFactoryItemDelegator(getAdapterFactory()).getText(collection.iterator().next());
					statusLineManager.setMessage(MessageFormat.format("Selected Object: {0}", text));
					break;
				default:
					statusLineManager.setMessage(MessageFormat.format("Selected {0} Objects", Integer.toString(collection.size())));
					break;
				}
			} else {
				statusLineManager.setMessage("");
			}
		}
	}

	/**
	 * This implements {@link org.eclipse.jface.action.IMenuListener} to help
	 * fill the context menus with contributions from the Edit menu.
	 */
	@Override
	public void menuAboutToShow(final IMenuManager menuManager) {
		((IMenuListener) getEditorSite().getActionBarContributor()).menuAboutToShow(menuManager);
	}

	@Override
	public void dispose() {
		final DeviceConfiguration dcd = getDeviceConfiguration();
		if (dcd != null) {
			dcd.eAdapters().remove(this.nameListener);
		}

		// Node listener dispose listener

		if (this.contentOutlinePage != null) {
			this.contentOutlinePage.dispose();
		}

		super.dispose();
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * org.eclipse.ui.views.properties.tabbed.ITabbedPropertySheetPageContributor
	 * #getContributorId()
	 */
	public String getContributorId() {
		if (this.diagramEditor != null) {
			return this.diagramEditor.getContributorId();
		} else {
			return null;
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * org.eclipse.gmf.runtime.diagram.ui.parts.IDiagramWorkbenchPart#getDiagram
	 * ()
	 */
	public Diagram getDiagram() {
		if (this.diagramEditor != null) {
			return this.diagramEditor.getDiagram();
		} else {
			return null;
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @seeorg.eclipse.gmf.runtime.diagram.ui.parts.IDiagramWorkbenchPart#
	 * getDiagramEditDomain()
	 */
	public IDiagramEditDomain getDiagramEditDomain() {
		if (this.diagramEditor != null) {
			return this.diagramEditor.getDiagramEditDomain();
		} else {
			return null;
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @seeorg.eclipse.gmf.runtime.diagram.ui.parts.IDiagramWorkbenchPart#
	 * getDiagramEditPart()
	 */
	public DiagramEditPart getDiagramEditPart() {
		if (this.diagramEditor != null) {
			return this.diagramEditor.getDiagramEditPart();
		} else {
			return null;
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @seeorg.eclipse.gmf.runtime.diagram.ui.parts.IDiagramWorkbenchPart#
	 * getDiagramGraphicalViewer()
	 */
	public IDiagramGraphicalViewer getDiagramGraphicalViewer() {
		if (this.diagramEditor != null) {
			return this.diagramEditor.getDiagramGraphicalViewer();
		} else {
			return null;
		}
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public String getTitle() {
		String name = null;
		final DeviceConfiguration dcd = getDeviceConfiguration();
		if (dcd != null) {
			name = dcd.getName();
			if (name == null) {
				name = getEditorInput().getName();
			}
		}
		if (name != null) {
			return name;
		} else {
			return super.getTitle();
		}
	}

	/**
	 * @return
	 */
	private DeviceConfiguration getDeviceConfiguration() {
		return ModelUtil.getDeviceConfiguration(getMainResource());
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	protected void addPages() {
		// Only creates the other pages if there is something that can be edited
		//
		if (!getEditingDomain().getResourceSet().getResources().isEmpty()
		        && !(getEditingDomain().getResourceSet().getResources().get(0)).getContents().isEmpty()) {

			try {
				int pageIndex;

				final URI diagramURI = DiagramUtil.getDiagramResourceURI(DcdDiagramUtilHelper.INSTANCE, getMainResource());

				DiagramUtil.initializeDiagramResource(DcdDiagramUtilHelper.INSTANCE, diagramURI, getMainResource());

				// This is the page for the graphical diagram viewer.
				//
				final IEditorInput diagramInput = DiagramUtil.getDiagramWrappedInput(diagramURI, (TransactionalEditingDomain) this.getEditingDomain());

				this.diagramEditor = new ExplorerDiagramEditor();
				pageIndex = addPage(this.diagramEditor, diagramInput);
				setPageText(pageIndex, "Diagram");

				try {
					this.dcdSourcePageNum = addPage(new TextEditor(), this.getEditorInput());
					this.setPageText(this.dcdSourcePageNum, this.getEditorInput().getName());
				} catch (final NullPointerException e) {
					// PASS
					// FIXME Why does this throw a null pointer when loaded from the server
				}

				getDeviceConfiguration().eAdapters().add(this.nameListener);
				final DeviceConfiguration activeNode = getDeviceConfiguration();
				if (activeNode != null) {
					activeNode.eAdapters().add(this.disposeListener);
				}
			} catch (final PartInitException e) {
				StatusManager.getManager().handle(new Status(IStatus.ERROR, NodeExplorerPlugin.getPluginID(), "Failed to create editor parts.", e),
				        StatusManager.LOG | StatusManager.SHOW);
			} catch (final IOException e) {
				StatusManager.getManager().handle(new Status(IStatus.ERROR, NodeExplorerPlugin.getPluginID(), "Failed to create editor parts.", e),
				        StatusManager.LOG | StatusManager.SHOW);
			} catch (final CoreException e) {
				StatusManager.getManager().handle(new Status(IStatus.ERROR, NodeExplorerPlugin.getPluginID(), "Failed to create editor parts.", e),
				        StatusManager.LOG | StatusManager.SHOW);
			}
		} else {
			final Label label = new Label(getContainer(), SWT.None);
			label.setText("Failed to load editor.");
			addPage(label);
		}
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	protected void handleDocumentChange(final Resource resource) {
		super.handleDocumentChange(resource);
		for (final Object part : this.getDiagramEditPart().getChildren()) {
			if (part instanceof EditPart) {
				((EditPart) part).refresh();
			}
		}
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	protected IContentOutlinePage createContentOutline() {
		return getContentOutlinePage();
	}

	/**
	 * This accesses a cached version of the content outliner.
	 */
	public IContentOutlinePage getContentOutlinePage() {
		if (this.contentOutlinePage != null) {
			// The content outline is just a tree.
			//
			class MyContentOutlinePage extends ContentOutlinePage {
				@Override
				public void createControl(final Composite parent) {
					super.createControl(parent);
					NodeEditor.this.contentOutlineViewer = getTreeViewer();
					NodeEditor.this.contentOutlineViewer.addSelectionChangedListener(this);

					// Set up the tree viewer.
					//
					NodeEditor.this.contentOutlineViewer.setContentProvider(new AdapterFactoryContentProvider(getAdapterFactory()));
					NodeEditor.this.contentOutlineViewer.setLabelProvider(new AdapterFactoryLabelProvider(getAdapterFactory()));
					NodeEditor.this.contentOutlineViewer.setInput(getEditingDomain().getResourceSet());

					// Make sure our popups work.
					//
					createContextMenuFor(NodeEditor.this.contentOutlineViewer);

					if (!getEditingDomain().getResourceSet().getResources().isEmpty()) {
						// Select the root object in the view.
						//
						NodeEditor.this.contentOutlineViewer.setSelection(new StructuredSelection(getEditingDomain().getResourceSet().getResources().get(0)),
						        true);
					}
				}

				@Override
				public void makeContributions(final IMenuManager menuManager, final IToolBarManager toolBarManager, final IStatusLineManager statusLineManager) {
					super.makeContributions(menuManager, toolBarManager, statusLineManager);
					NodeEditor.this.contentOutlineStatusLineManager = statusLineManager;
				}

				@Override
				public void setActionBars(final IActionBars actionBars) {
					super.setActionBars(actionBars);
					// TODO
					// getMyActionBarContributor().shareGlobalActions(this,
					// actionBars);
				}
			}

			this.contentOutlinePage = new MyContentOutlinePage();

			// Listen to selection so that we can handle it is a special way.
			//
			this.contentOutlinePage.addSelectionChangedListener(new ISelectionChangedListener() {
				// This ensures that we handle selections correctly.
				//
				public void selectionChanged(final SelectionChangedEvent event) {
					handleContentOutlineSelection(event.getSelection());
				}
			});
		}
		return this.contentOutlinePage;
	}

	/**
	 * This deals with how we want selection in the outliner to affect the other
	 * views.
	 */
	@SuppressWarnings("unchecked")
	public void handleContentOutlineSelection(final ISelection selection) {
		if (!selection.isEmpty() && selection instanceof IStructuredSelection) {
			final List< ? > selectedElements = ((IStructuredSelection) selection).toList();
			if (getActiveEditor() == this.diagramEditor) {
				// If the diagram viewer is active, we need to map the selection
				// to the corresponding EditParts.
				//
				final ArrayList<Object> selectionList = new ArrayList<Object>();
				for (final Object selectedElement : selectedElements) {
					if (selectedElement instanceof EObject) {
						final String elementID = EMFCoreUtil.getProxyID((EObject) selectedElement);
						selectionList.addAll(this.diagramEditor.getDiagramGraphicalViewer().findEditPartsForElement(elementID, IGraphicalEditPart.class));
					}
					this.selectionProvider.setSelection(new StructuredSelection(selectionList));
				}
			}
		}
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public String getEditingDomainId() {
		return NodeEditor.EDITING_DOMAIN_ID;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	protected AdapterFactory getSpecificAdapterFactory() {
		final ComposedAdapterFactory factory = new ComposedAdapterFactory();
		factory.addAdapterFactory(new DcdItemProviderAdapterFactory());
		factory.addAdapterFactory(new EcoreItemProviderAdapterFactory());
		factory.addAdapterFactory(new SpdItemProviderAdapterFactory());
		factory.addAdapterFactory(new ScdItemProviderAdapterFactory());
		factory.addAdapterFactory(new PrfItemProviderAdapterFactory());
		return factory;
	}

	public IActionBars getActionBars() {
		return getActionBarContributor().getActionBars();
	}

	@Override
	public List<Object> getOutlineItems() {
		return null;
	}

	@Override
	protected void emfDoSave(final IProgressMonitor progressMonitor) {
		// Refresh the necessary state. We are delegating the save to the diagram page
		//
		((BasicCommandStack) getEditingDomain().getCommandStack()).saveIsDone();
	}

	@Override
	public boolean isPersisted(final Resource resource) {
		return resource.getURI().equals(getDeviceConfiguration().eResource().getURI()) && super.isPersisted(resource);
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public boolean isDirty() {
		return false;
	}

	@Override
	public void doSave(final IProgressMonitor monitor) {
		throw new UnsupportedOperationException();
	}
}
