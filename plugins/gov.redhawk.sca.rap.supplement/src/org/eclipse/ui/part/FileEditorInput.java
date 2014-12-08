/** 
 * This file is protected by Copyright. 
 * Please refer to the COPYRIGHT file distributed with this source distribution.
 * 
 * This file is part of REDHAWK IDE.
 * 
 * All rights reserved.  This program and the accompanying materials are made available under 
 * the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html.
 *
 * 
 * Copyright (c) 2000, 2008 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     IBM Corporation - initial API and implementation
 *******************************************************************************/
package org.eclipse.ui.part;


import java.net.URI;

import org.eclipse.core.filesystem.EFS;
import org.eclipse.core.filesystem.IFileStore;

import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IPath;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.PlatformObject;
import org.eclipse.core.runtime.content.IContentDescription;
import org.eclipse.core.runtime.content.IContentType;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IResourceStatus;
import org.eclipse.core.resources.IStorage;

import org.eclipse.jface.resource.ImageDescriptor;

import org.eclipse.ui.IFileEditorInput;
import org.eclipse.ui.IMemento;
import org.eclipse.ui.IPathEditorInput;
import org.eclipse.ui.IPersistableElement;
import org.eclipse.ui.IURIEditorInput;
import org.eclipse.ui.PlatformUI;
import org.eclipse.ui.internal.misc.UIStats;
import org.eclipse.ui.model.IWorkbenchAdapter;

/**
 * Adapter for making a file resource a suitable input for an editor.
 * <p>
 * This class may be instantiated; it is not intended to be subclassed.
 * </p>
 * @noextend This class is not intended to be subclassed by clients.
 * @since 7.0
 */
public class FileEditorInput extends PlatformObject implements IFileEditorInput, IPathEditorInput, IURIEditorInput,
		IPersistableElement {
	private IFile file;
	
	/**
	 * Return whether or not file is local. Only {@link IFile}s with a local
	 * value should call {@link IPathEditorInput#getPath()}
	 * @param file
	 * @return boolean <code>true</code> if the file has a local implementation.
	 * @since 3.4
	 */
	public static boolean isLocalFile(IFile file) {

		IPath location = file.getLocation();
		if (location != null)
			return true;
		//this is not a local file, so try to obtain a local file
		try {
	        final URI locationURI = file.getLocationURI();
	        if (locationURI == null)
	           return false;
	        IFileStore store = EFS.getStore(locationURI);
			//first try to obtain a local file directly fo1r this store
			java.io.File localFile = store.toLocalFile(EFS.NONE, null);
			//if no local file is available, obtain a cached file
			if (localFile == null)
				localFile = store.toLocalFile(EFS.CACHE, null);
			if (localFile == null)
				return false;
			return true;
		} catch (CoreException e) {
			//this can only happen if the file system is not available for this scheme
			//TODO implement log for RAP
//			IDEWorkbenchPlugin.log(
//					"Failed to obtain file store for resource", e); //$NON-NLS-1$
			return false;
		}
	
	}

	/**
	 * Creates an editor input based of the given file resource.
	 *
	 * @param file the file resource
	 */
	public FileEditorInput(IFile file) {
		if (file == null)
			throw new IllegalArgumentException();
		this.file = file;
	
	}

	/* (non-Javadoc)
	 * Method declared on Object.
	 */
	public int hashCode() {
		return file.hashCode();
	}

	/* (non-Javadoc)
	 * Method declared on Object.
	 *
	 * The <code>FileEditorInput</code> implementation of this <code>Object</code>
	 * method bases the equality of two <code>FileEditorInput</code> objects on the
	 * equality of their underlying <code>IFile</code> resources.
	 */
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!(obj instanceof IFileEditorInput)) {
			return false;
		}
		IFileEditorInput other = (IFileEditorInput) obj;
		return file.equals(other.getFile());
	}

	/* (non-Javadoc)
	 * Method declared on IEditorInput.
	 */
	public boolean exists() {
		return file.exists();
	}

	/* (non-Javadoc)
	 * Method declared on IPersistableElement.
	 */
	public String getFactoryId() {
		return FileEditorInputFactory.getFactoryId();
	}

	/* (non-Javadoc)
	 * Method declared on IFileEditorInput.
	 */
	public IFile getFile() {
		return file;
	}

	/* (non-Javadoc)
	 * Method declared on IEditorInput.
	 */
	public ImageDescriptor getImageDescriptor() {
		IContentType contentType = getContentType(file);
		return PlatformUI.getWorkbench().getEditorRegistry()
				.getImageDescriptor(file.getName(), contentType);
	}

	/**
	 * Copied from org.eclipse.ui.IDE
	 * 
	 * Return the content type for the given file.
	 * 
	 * @param file
	 *            the file to test
	 * @return the content type, or <code>null</code> if it cannot be
	 *         determined.
	 * @since 3.1
	 */
	public static IContentType getContentType(IFile file) {
		try {
			UIStats.start(UIStats.CONTENT_TYPE_LOOKUP, file.getName());
			IContentDescription contentDescription = file
					.getContentDescription();
			if (contentDescription == null) {
				return null;
			}
			return contentDescription.getContentType();
		} catch (CoreException e) {
			if (e.getStatus().getCode() == IResourceStatus.OUT_OF_SYNC_LOCAL) {
				// Determine the content type from the file name.
				return Platform.getContentTypeManager()
							.findContentTypeFor(file.getName());
			}
			return null;
		} finally {
			UIStats.end(UIStats.CONTENT_TYPE_LOOKUP, file, file.getName());
		}
	}

	/* (non-Javadoc)
	 * Method declared on IEditorInput.
	 */
	public String getName() {
		return file.getName();
	}

	/* (non-Javadoc)
	 * Method declared on IEditorInput.
	 */
	public IPersistableElement getPersistable() {
		return this;
	}

	/* (non-Javadoc)
	 * Method declared on IStorageEditorInput.
	 */
	public IStorage getStorage() {
		return file;
	}

	/* (non-Javadoc)
	 * Method declared on IEditorInput.
	 */
	public String getToolTipText() {
		return file.getFullPath().makeRelative().toString();
	}

	/* (non-Javadoc)
	 * Method declared on IPersistableElement.
	 */
	public void saveState(IMemento memento) {
		FileEditorInputFactory.saveState(memento, this);
	}

	

	/* (non-Javadoc)
	 * @see org.eclipse.ui.IURIEditorInput#getURI()
	 */
	public URI getURI() {
		return file.getLocationURI();
	}
	
	
	/* (non-Javadoc)
	 * @see org.eclipse.ui.IPathEditorInput#getPath()
	 */
	public IPath getPath() {
		IPath location = file.getLocation();
		if (location != null)
			return location;
		//this is not a local file, so try to obtain a local file
		try {
	        final URI locationURI = file.getLocationURI();
	        if (locationURI == null)
	           throw new IllegalArgumentException();
	        IFileStore store = EFS.getStore(locationURI);
			//first try to obtain a local file directly fo1r this store
			java.io.File localFile = store.toLocalFile(EFS.NONE, null);
			//if no local file is available, obtain a cached file
			if (localFile == null)
				localFile = store.toLocalFile(EFS.CACHE, null);
			if (localFile == null)
				throw new IllegalArgumentException();
			return Path.fromOSString(localFile.getAbsolutePath());
		} catch (CoreException e) {
			//this can only happen if the file system is not available for this scheme
			//TODO Implement logging for RAP
//			IDEWorkbenchPlugin.log(
//					"Failed to obtain file store for resource", e); //$NON-NLS-1$
			throw new RuntimeException(e);
		}
	}


	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString() {
		return getClass().getName() + "(" + getFile().getFullPath() + ")"; //$NON-NLS-1$ //$NON-NLS-2$
	}
	
	/*
	 * Allows for the return of an {@link IWorkbenchAdapter} adapter.
	 * 
	 * @since 3.5
	 * 
	 * @see org.eclipse.core.runtime.PlatformObject#getAdapter(java.lang.Class)
	 */
	public Object getAdapter(Class adapter) {
		if (IWorkbenchAdapter.class.equals(adapter)) {
			return new IWorkbenchAdapter() {

				public Object[] getChildren(Object o) {
					return new Object[0];
				}

				public ImageDescriptor getImageDescriptor(Object object) {
					return FileEditorInput.this.getImageDescriptor();
				}

				public String getLabel(Object o) {
					return FileEditorInput.this.getName();
				}

				public Object getParent(Object o) {
					return FileEditorInput.this.getFile().getParent();
				}
			};
		}

		return super.getAdapter(adapter);
	}
}