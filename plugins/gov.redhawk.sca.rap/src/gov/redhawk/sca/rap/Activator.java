package gov.redhawk.sca.rap;
import org.eclipse.core.runtime.Plugin;
import org.osgi.framework.BundleContext;


public class Activator extends Plugin {

	private static Activator plugin;
	private static BundleContext bundleContext;

	@Override
	public void start(BundleContext context) throws Exception {
		super.start(context);
		Activator.bundleContext = context;
		Activator.plugin = this;
	}

	@Override
	public void stop(BundleContext context) throws Exception {
		super.stop(context);
		Activator.bundleContext = null;
		Activator.plugin = null;
	}
	
	 /* Returns the shared instance.
	 * 
	 * @return the shared instance
	 */
	public static Activator getDefault() {
		return Activator.plugin;
	}
	
	public static BundleContext getBudleContext() {
		return Activator.bundleContext;
	}

}
