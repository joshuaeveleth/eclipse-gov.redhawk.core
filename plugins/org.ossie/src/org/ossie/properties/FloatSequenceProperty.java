/*
 * This file is protected by Copyright. Please refer to the COPYRIGHT file 
 * distributed with this source distribution.
 * 
 * This file is part of REDHAWK core.
 * 
 * REDHAWK core is free software: you can redistribute it and/or modify it 
 * under the terms of the GNU Lesser General Public License as published by the 
 * Free Software Foundation, either version 3 of the License, or (at your 
 * option) any later version.
 * 
 * REDHAWK core is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License 
 * for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this program.  If not, see http://www.gnu.org/licenses/.
 */

/*
 * WARNING: This file is generated from NumericSequenceProperty.template.
 *          Do not modify directly.
 */

package org.ossie.properties;

import java.util.List;

import org.omg.CORBA.Any;
import org.omg.CORBA.FloatSeqHelper;

public class FloatSequenceProperty extends NumericSequenceProperty<Float> {
    public FloatSequenceProperty(String id, String name, List<Float> value, Mode mode,
                                   Action action, Kind[] kinds) {
        super(id, name, "float", value, mode, action, kinds);
    }

    public FloatSequenceProperty(String id, String name, List<Float> value, Mode mode,
                                   Action action, Kind[] kinds, boolean optional) {
        super(id, name, "float", value, mode, action, kinds, optional);
    }

    public static List<Float> asList(Number... array) {
        return PrimitiveArrayUtils.convertToFloatList(array);
    }

    protected List<Float> fromNumberArray(Number[] array) {
        return PrimitiveArrayUtils.convertToFloatList(array);
    }

    protected void insert(Any any, List<Float> value) {
        FloatSeqHelper.insert(any, PrimitiveArrayUtils.convertToFloatArray(value));
    }
}
