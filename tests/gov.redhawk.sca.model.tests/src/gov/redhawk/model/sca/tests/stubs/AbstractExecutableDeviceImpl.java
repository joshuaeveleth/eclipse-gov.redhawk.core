package gov.redhawk.model.sca.tests.stubs;

import org.omg.CORBA.ORB;
import org.omg.PortableServer.POA;
import org.omg.PortableServer.POAPackage.ServantNotActive;
import org.omg.PortableServer.POAPackage.WrongPolicy;

import CF.DataType;
import CF.ExecutableDeviceOperations;
import CF.InvalidFileName;
import CF.DevicePackage.InvalidState;
import CF.ExecutableDevicePackage.ExecuteFail;
import CF.ExecutableDevicePackage.InvalidFunction;
import CF.ExecutableDevicePackage.InvalidOptions;
import CF.ExecutableDevicePackage.InvalidParameters;
import CF.ExecutableDevicePackage.InvalidProcess;

public class AbstractExecutableDeviceImpl extends AbstractLoadableDeviceImpl
		implements ExecutableDeviceOperations {

	public AbstractExecutableDeviceImpl() {
		super();
		// TODO Auto-generated constructor stub
	}

	public AbstractExecutableDeviceImpl(String compId, String compName,
			ORB orb, POA poa) throws ServantNotActive, WrongPolicy {
		super(compId, compName, orb, poa);
		// TODO Auto-generated constructor stub
	}

	public void terminate(int processId) throws InvalidProcess, InvalidState {
		// TODO Auto-generated method stub

	}

	public int execute(String name, DataType[] options, DataType[] parameters)
			throws InvalidState, InvalidFunction, InvalidParameters,
			InvalidOptions, InvalidFileName, ExecuteFail {
		// TODO Auto-generated method stub
		return 0;
	}

}
