/*******************************************************************************
 * This file is protected by Copyright. 
 * Please refer to the COPYRIGHT file distributed with this source distribution.
 *
 * This file is part of REDHAWK IDE.
 *
 * All rights reserved.  This program and the accompanying materials are made available under 
 * the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at 
 * http://www.eclipse.org/legal/epl-v10.html
 *******************************************************************************/

 // BEGIN GENERATED CODE
package gov.redhawk.model.sca.provider;

import gov.redhawk.model.sca.util.ScaAdapterFactory;

import java.util.ArrayList;
import java.util.Collection;

import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.Notifier;
import org.eclipse.emf.edit.provider.ChangeNotifier;
import org.eclipse.emf.edit.provider.ComposeableAdapterFactory;
import org.eclipse.emf.edit.provider.ComposedAdapterFactory;
import org.eclipse.emf.edit.provider.Disposable;
import org.eclipse.emf.edit.provider.IChangeNotifier;
import org.eclipse.emf.edit.provider.IDisposable;
import org.eclipse.emf.edit.provider.IEditingDomainItemProvider;
import org.eclipse.emf.edit.provider.IItemColorProvider;
import org.eclipse.emf.edit.provider.IItemLabelProvider;
import org.eclipse.emf.edit.provider.IItemPropertySource;
import org.eclipse.emf.edit.provider.INotifyChangedListener;
import org.eclipse.emf.edit.provider.IStructuredItemContentProvider;
import org.eclipse.emf.edit.provider.ITableItemColorProvider;
import org.eclipse.emf.edit.provider.ITableItemLabelProvider;
import org.eclipse.emf.edit.provider.ITreeItemContentProvider;

/**
 * This is the factory that is used to provide the interfaces needed to support Viewers.
 * The adapters generated by this factory convert EMF adapter notifications into calls to {@link #fireNotifyChanged fireNotifyChanged}.
 * The adapters also support Eclipse property sheets.
 * Note that most of the adapters are shared among multiple instances.
 * <!-- begin-user-doc --> <!--
 * end-user-doc -->
 * @generated
 */
public class ScaItemProviderAdapterFactory extends ScaAdapterFactory implements ComposeableAdapterFactory, IChangeNotifier, IDisposable {

	/**
	 * This keeps track of the root adapter factory that delegates to this adapter factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ComposedAdapterFactory parentAdapterFactory;
	/**
	 * This is used to implement {@link org.eclipse.emf.edit.provider.IChangeNotifier}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected IChangeNotifier changeNotifier = new ChangeNotifier();
	/**
	 * This keeps track of all the item providers created, so that they can be {@link #dispose disposed}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected Disposable disposable = new Disposable();
	/**
	 * This keeps track of all the supported types checked by {@link #isFactoryForType isFactoryForType}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected Collection<Object> supportedTypes = new ArrayList<Object>();

	/**
	 * This constructs an instance.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public ScaItemProviderAdapterFactory() {
		supportedTypes.add(IEditingDomainItemProvider.class);
		supportedTypes.add(IStructuredItemContentProvider.class);
		supportedTypes.add(ITreeItemContentProvider.class);
		supportedTypes.add(IItemLabelProvider.class);
		supportedTypes.add(IItemPropertySource.class);
		supportedTypes.add(ITableItemLabelProvider.class);
		supportedTypes.add(ITableItemColorProvider.class);
		supportedTypes.add(IItemColorProvider.class);
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.Properties} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected PropertiesItemProvider propertiesItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.Properties}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createPropertiesAdapter() {
		if (propertiesItemProvider == null) {
			propertiesItemProvider = new PropertiesItemProvider(this);
		}

		return propertiesItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaComponent} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaComponentItemProvider scaComponentItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaComponent}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaComponentAdapter() {
		if (scaComponentItemProvider == null) {
			scaComponentItemProvider = new ScaComponentItemProvider(this);
		}

		return scaComponentItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDevice} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDeviceItemProvider scaDeviceItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDevice}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDeviceAdapter() {
		if (scaDeviceItemProvider == null) {
			scaDeviceItemProvider = new ScaDeviceItemProvider(this);
		}

		return scaDeviceItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDeviceManager} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDeviceManagerItemProvider scaDeviceManagerItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDeviceManager}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDeviceManagerAdapter() {
		if (scaDeviceManagerItemProvider == null) {
			scaDeviceManagerItemProvider = new ScaDeviceManagerItemProvider(this);
		}

		return scaDeviceManagerItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaService} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaServiceItemProvider scaServiceItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaService}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaServiceAdapter() {
		if (scaServiceItemProvider == null) {
			scaServiceItemProvider = new ScaServiceItemProvider(this);
		}

		return scaServiceItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDeviceManagerFileSystem} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDeviceManagerFileSystemItemProvider scaDeviceManagerFileSystemItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDeviceManagerFileSystem}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDeviceManagerFileSystemAdapter() {
		if (scaDeviceManagerFileSystemItemProvider == null) {
			scaDeviceManagerFileSystemItemProvider = new ScaDeviceManagerFileSystemItemProvider(this);
		}

		return scaDeviceManagerFileSystemItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDocumentRoot} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDocumentRootItemProvider scaDocumentRootItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDocumentRoot}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDocumentRootAdapter() {
		if (scaDocumentRootItemProvider == null) {
			scaDocumentRootItemProvider = new ScaDocumentRootItemProvider(this);
		}

		return scaDocumentRootItemProvider;
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDomainManager}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDomainManagerAdapter() {
		return new ScaDomainManagerItemProvider(this);
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDomainManagerFileSystem} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDomainManagerFileSystemItemProvider scaDomainManagerFileSystemItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDomainManagerFileSystem}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDomainManagerFileSystemAdapter() {
		if (scaDomainManagerFileSystemItemProvider == null) {
			scaDomainManagerFileSystemItemProvider = new ScaDomainManagerFileSystemItemProvider(this);
		}

		return scaDomainManagerFileSystemItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaDomainManagerRegistry} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaDomainManagerRegistryItemProvider scaDomainManagerRegistryItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaDomainManagerRegistry}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaDomainManagerRegistryAdapter() {
		if (scaDomainManagerRegistryItemProvider == null) {
			scaDomainManagerRegistryItemProvider = new ScaDomainManagerRegistryItemProvider(this);
		}

		return scaDomainManagerRegistryItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaExecutableDevice} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaExecutableDeviceItemProvider scaExecutableDeviceItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaExecutableDevice}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaExecutableDeviceAdapter() {
		if (scaExecutableDeviceItemProvider == null) {
			scaExecutableDeviceItemProvider = new ScaExecutableDeviceItemProvider(this);
		}

		return scaExecutableDeviceItemProvider;
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaFileStore}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaFileStoreAdapter() {
		return new ScaFileStoreItemProvider(this);
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaLoadableDevice} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaLoadableDeviceItemProvider scaLoadableDeviceItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaLoadableDevice}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaLoadableDeviceAdapter() {
		if (scaLoadableDeviceItemProvider == null) {
			scaLoadableDeviceItemProvider = new ScaLoadableDeviceItemProvider(this);
		}

		return scaLoadableDeviceItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaProvidesPort} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaProvidesPortItemProvider scaProvidesPortItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaProvidesPort}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaProvidesPortAdapter() {
		if (scaProvidesPortItemProvider == null) {
			scaProvidesPortItemProvider = new ScaProvidesPortItemProvider(this);
		}

		return scaProvidesPortItemProvider;
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaSimpleProperty}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaSimplePropertyAdapter() {
		return new ScaSimplePropertyItemProvider(this);
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaSimpleSequenceProperty}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaSimpleSequencePropertyAdapter() {
		return new ScaSimpleSequencePropertyItemProvider(this);
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaStructProperty}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaStructPropertyAdapter() {
		return new ScaStructPropertyItemProvider(this);
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaUsesPort} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaUsesPortItemProvider scaUsesPortItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaUsesPort}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaUsesPortAdapter() {
		if (scaUsesPortItemProvider == null) {
			scaUsesPortItemProvider = new ScaUsesPortItemProvider(this);
		}

		return scaUsesPortItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaConnection} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaConnectionItemProvider scaConnectionItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaConnection}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaConnectionAdapter() {
		if (scaConnectionItemProvider == null) {
			scaConnectionItemProvider = new ScaConnectionItemProvider(this);
		}

		return scaConnectionItemProvider;
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaWaveform}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaWaveformAdapter() {
		return new ScaWaveformItemProvider(this);
	}

	/**
	 * This keeps track of the one adapter used for all {@link gov.redhawk.model.sca.ScaWaveformFactory} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected ScaWaveformFactoryItemProvider scaWaveformFactoryItemProvider;

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaWaveformFactory}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaWaveformFactoryAdapter() {
		if (scaWaveformFactoryItemProvider == null) {
			scaWaveformFactoryItemProvider = new ScaWaveformFactoryItemProvider(this);
		}

		return scaWaveformFactoryItemProvider;
	}

	/**
	 * This keeps track of the one adapter used for all {@link java.util.Map.Entry} instances.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected StringToStringMapItemProvider stringToStringMapItemProvider;

	/**
	 * This creates an adapter for a {@link java.util.Map.Entry}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createStringToStringMapAdapter() {
		if (stringToStringMapItemProvider == null) {
			stringToStringMapItemProvider = new StringToStringMapItemProvider(this);
		}

		return stringToStringMapItemProvider;
	}

	/**
	 * This creates an adapter for a {@link gov.redhawk.model.sca.ScaStructSequenceProperty}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter createScaStructSequencePropertyAdapter() {
		return new ScaStructSequencePropertyItemProvider(this);
	}

	/**
	 * This returns the root adapter factory that contains this factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public ComposeableAdapterFactory getRootAdapterFactory() {
		return parentAdapterFactory == null ? this : parentAdapterFactory.getRootAdapterFactory();
	}

	/**
	 * This sets the composed adapter factory that contains this factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setParentAdapterFactory(ComposedAdapterFactory parentAdapterFactory) {
		this.parentAdapterFactory = parentAdapterFactory;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean isFactoryForType(Object type) {
		return supportedTypes.contains(type) || super.isFactoryForType(type);
	}

	/**
	 * This implementation substitutes the factory itself as the key for the adapter.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Adapter adapt(Notifier notifier, Object type) {
		return super.adapt(notifier, this);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object adapt(Object object, Object type) {
		if (isFactoryForType(type)) {
			Object adapter = super.adapt(object, type);
			if (!(type instanceof Class<?>) || (((Class<?>)type).isInstance(adapter))) {
				return adapter;
			}
		}

		return null;
	}

	/**
	 * Associates an adapter with a notifier via the base implementation, then records it to ensure it will be disposed.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected void associate(Adapter adapter, Notifier target) {
		super.associate(adapter, target);
		if (adapter != null) {
			disposable.add(adapter);
		}
	}

	/**
	 * This adds a listener.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void addListener(INotifyChangedListener notifyChangedListener) {
		changeNotifier.addListener(notifyChangedListener);
	}

	/**
	 * This removes a listener.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void removeListener(INotifyChangedListener notifyChangedListener) {
		changeNotifier.removeListener(notifyChangedListener);
	}

	/**
	 * This delegates to {@link #changeNotifier} and to {@link #parentAdapterFactory}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void fireNotifyChanged(Notification notification) {
		changeNotifier.fireNotifyChanged(notification);

		if (parentAdapterFactory != null) {
			parentAdapterFactory.fireNotifyChanged(notification);
		}
	}

	/**
	 * This disposes all of the item providers created by this factory. 
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void dispose() {
		disposable.dispose();
	}

}
