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
package gov.redhawk.sca.dcd.diagram.edit.policies;

import gov.redhawk.diagram.edit.commands.FindByStubCreateCommand;
import gov.redhawk.sca.dcd.diagram.edit.commands.ComponentPlacementCreateCommand;
import gov.redhawk.sca.dcd.diagram.providers.RedhawkDcdElementTypes;
import mil.jpeojtrs.sca.dcd.DeviceConfiguration;
import mil.jpeojtrs.sca.dcd.diagram.providers.DcdElementTypes;

import org.eclipse.gef.commands.Command;
import org.eclipse.gmf.runtime.emf.type.core.commands.MoveElementsCommand;
import org.eclipse.gmf.runtime.emf.type.core.requests.CreateElementRequest;
import org.eclipse.gmf.runtime.emf.type.core.requests.DestroyRequest;
import org.eclipse.gmf.runtime.emf.type.core.requests.MoveRequest;

/**
 * 
 */
public class DeviceConfigurationEditPartItemSemanticEditPolicy extends mil.jpeojtrs.sca.dcd.diagram.edit.policies.DeviceConfigurationItemSemanticEditPolicy {

	@Override
	protected Command getCreateCommand(final CreateElementRequest req) {
		if (DcdElementTypes.DcdComponentPlacement_3001 == req.getElementType()) {
			return getGEFWrapper(new ComponentPlacementCreateCommand(req));
		} else if (DcdElementTypes.DcdPartitioning_2001 == req.getElementType()) {
			// Return null here since we want to disable adding partitions
			return null;
		} else if (RedhawkDcdElementTypes.FindByStub == req.getElementType()) {
			final FindByStubCreateCommand command = new FindByStubCreateCommand(req);
			command.setEditPart(getHost());
			return getGEFWrapper(command);
		}
		return super.getCreateCommand(req);
	}

	@Override
	protected Command getMoveCommand(final MoveRequest req) {
		final DeviceConfiguration dcd = (DeviceConfiguration) req.getTargetContainer();
		req.setTargetContainer(dcd.getPartitioning());
		return getGEFWrapper(new MoveElementsCommand(req));
	}

	@Override
	protected boolean shouldProceed(final DestroyRequest destroyRequest) {
		return false;
	}

}
