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
 */
package gov.redhawk.sca.preferences;

import gov.redhawk.model.sca.ScaDomainManager;
import gov.redhawk.model.sca.ScaDomainManagerRegistry;
import gov.redhawk.model.sca.ScaFactory;
import gov.redhawk.sca.ScaPlugin;
import gov.redhawk.sca.util.CorbaURIUtil;
import gov.redhawk.sca.util.IPreferenceAccessor;

import java.io.IOException;
import java.net.URL;
import java.util.Collections;
import java.util.Map;

import mil.jpeojtrs.sca.util.ScaResourceFactoryUtil;

import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.preferences.AbstractPreferenceInitializer;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.osgi.service.datalocation.Location;

/**
 * The Class RedhawkIdePreferenceInitializer.
 */
public class ScaPreferenceInitializer extends AbstractPreferenceInitializer {

	private static ScaDomainManagerRegistry scaDomainManagerRegistry;

	/**
	 * Instantiates a new REDHAWK SCA preference initializer.
	 */
	public ScaPreferenceInitializer() {
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public void initializeDefaultPreferences() {
		final IPreferenceAccessor accessor = ScaPlugin.getDefault().getScaPreferenceAccessor();

		accessor.setDefault(ScaPreferenceConstants.SCA_CORBA_AUTOCONNECT_PREFERENCE, true);
		accessor.setDefault(ScaPreferenceConstants.SCA_DEFAULT_NAMING_SERVICE, "corbaname::localhost:2809");
		accessor.setDefault(ScaPreferenceConstants.SCA_DOMAIN_WAVEFORMS_SEARCH_PATH, ScaPreferenceConstants.createPath(new String[] {
			"waveforms"
		}));
	}

	/**
	 * Loads a default configuration of domains.  This is loaded from the domains.sca file located in the configuration.
	 * It is also populated with the values from the preference store to support backwards compatibility.
	 * 
	 * We do not need to create the file if it doesn't exist, simple create one in the memory file store.
	 * @since 3.0
	 */
	public static ScaDomainManagerRegistry getDefaultScaDomainManagerRegistry() {
		if (ScaPreferenceInitializer.scaDomainManagerRegistry == null) {
			synchronized (ScaPreferenceInitializer.class) {
				if (ScaPreferenceInitializer.scaDomainManagerRegistry == null) { // SUPPRESS CHECKSTYLE DoubleCheck
					final ResourceSet resourceSet = ScaResourceFactoryUtil.createResourceSet();
					try {
						// First, try the user's config area
						final URL configUrl = ScaPreferenceInitializer.getDomainManagerRegistryConfigURL();
						final org.eclipse.emf.common.util.URI configUri = org.eclipse.emf.common.util.URI.createURI(configUrl.toString());
						final Resource configResource = resourceSet.getResource(configUri, true);
						ScaPreferenceInitializer.scaDomainManagerRegistry = ScaDomainManagerRegistry.Util.getScaDomainManagerRegistry(configResource);
					} catch (final Exception e1) {
						// Second, try the shared config area
						try {
							final URL sharedConfigUrl = ScaPreferenceInitializer.getDomainManagerRegistrySharedConfigURL();
							if (sharedConfigUrl != null) {
								final org.eclipse.emf.common.util.URI sharedConfigUri = org.eclipse.emf.common.util.URI.createURI(sharedConfigUrl.toString());
								final Resource sharedConfigResource = resourceSet.getResource(sharedConfigUri, true);
								ScaPreferenceInitializer.scaDomainManagerRegistry = ScaDomainManagerRegistry.Util.getScaDomainManagerRegistry(sharedConfigResource);
							}
						} catch (final Exception e2) {
							// PASS
						}
					}

					// If we still don't have a registry, create a new one from defaults
					if (ScaPreferenceInitializer.scaDomainManagerRegistry == null) { // SUPPRESS CHECKSTYLE DoubleCheck
						ScaPreferenceInitializer.scaDomainManagerRegistry = ScaFactory.eINSTANCE.createScaDomainManagerRegistry();
						final Resource resource = resourceSet.createResource(org.eclipse.emf.common.util.URI.createURI("virtual://domains.sca"));
						resource.getContents().add(ScaPreferenceInitializer.scaDomainManagerRegistry);
						ScaPreferenceInitializer.initFromPreference(ScaPreferenceInitializer.scaDomainManagerRegistry);
					}
				}
			}

		}
		return ScaPreferenceInitializer.scaDomainManagerRegistry;
	}

	/**
	 * Gets the URL for the domain manager registry within the user's configuration
	 * @return
	 */
	private static URL getDomainManagerRegistryConfigURL() {
		final Location configurationLocation = Platform.getConfigurationLocation();
		if (configurationLocation == null) {
			return null;
		}
		try {
			return configurationLocation.getDataArea(ScaPlugin.PLUGIN_ID + "/domains.sca");
		} catch (final IOException e) {
			return null;
		}
	}

	/**
	 * Gets the URL for the domain manager registry with the application's configuration
	 * @return
	 */
	private static URL getDomainManagerRegistrySharedConfigURL() {
		final Location configLocation = Platform.getConfigurationLocation();
		if (configLocation == null) {
			return null;
		}
		final Location sharedConfigLocation = configLocation.getParentLocation();
		if (sharedConfigLocation == null) {
			return null;
		}
		try {
			return sharedConfigLocation.getDataArea(ScaPlugin.PLUGIN_ID + "/domains.sca");
		} catch (final IOException e) {
			return null;
		}
	}

	private static void initFromPreference(final ScaDomainManagerRegistry retVal) {
		final ScaDomainConnectionDef[] connections = ScaPreferenceUtil.loadDomainConnections();
		for (final ScaDomainConnectionDef def : connections) {

			String nameServiceRef = def.getNameServiceInitRef();
			nameServiceRef = CorbaURIUtil.addDefaultPrefix(nameServiceRef);
			nameServiceRef = CorbaURIUtil.addDefaultPort(nameServiceRef);
			final Map<String, String> connectionProperties = Collections.singletonMap(ScaDomainManager.NAMING_SERVICE_PROP, nameServiceRef);
			retVal.createDomain(def.getDomainName(), false, connectionProperties);
		}

	}
}
