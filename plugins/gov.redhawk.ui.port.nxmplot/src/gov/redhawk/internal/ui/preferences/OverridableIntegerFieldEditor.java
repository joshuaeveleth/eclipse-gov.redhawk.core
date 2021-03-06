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
package gov.redhawk.internal.ui.preferences;

import org.eclipse.jdt.annotation.NonNull;
import org.eclipse.jface.preference.IntegerFieldEditor;
import org.eclipse.jface.resource.ColorRegistry;
import org.eclipse.jface.resource.JFaceResources;
import org.eclipse.swt.events.FocusEvent;
import org.eclipse.swt.events.FocusListener;
import org.eclipse.swt.events.ModifyEvent;
import org.eclipse.swt.events.ModifyListener;
import org.eclipse.swt.graphics.Color;
import org.eclipse.swt.graphics.RGB;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Text;

public class OverridableIntegerFieldEditor extends IntegerFieldEditor {

	/** max digits for a 32-bit integer (including minus sign) is 11 */
	static final int DEFAULT_TEXT_LIMIT = 11;
	
	private String overridePrefName;
	private boolean override;
	private ModifyListener listener = new ModifyListener() {

		@Override
		public void modifyText(ModifyEvent e) {
			String textStr = getTextControl().getText();
			if (textStr.isEmpty() || textStr.toUpperCase().startsWith("AUTO")) {
				override = false;
			} else {
				override = true;
			}
			updateTextFieldColor();
		}
	};
	private Color defaultForeground;
	private Color disabledForeground;
	private String autoTextValue;

	public OverridableIntegerFieldEditor(String name, String nameOverride, String labelText, Composite parent) {
		this(name, nameOverride, labelText, null, parent);
	}
	
	public OverridableIntegerFieldEditor(String name, String nameOverride, String labelText, String autoValue, Composite parent) {
		super(name, labelText, parent, DEFAULT_TEXT_LIMIT);
		this.overridePrefName = nameOverride;
		setAutoValue(autoValue);
		final Text textControl = getTextControl();
		textControl.addModifyListener(listener);
		textControl.addFocusListener(new FocusListener() {

			@Override
			public void focusLost(FocusEvent e) {
				if (!override) {
					textControl.setText(getAutoValueForText());
				}
			}

			@Override
			public void focusGained(FocusEvent e) {
				if (!override) {
					textControl.setText("");
				}
			}
		});
		setEmptyStringAllowed(true);
		initColors(textControl);
		updateTextFieldColor();
	}

	public void setToolTipText(String val) {
		Text textControl = getTextControl();
		if (textControl != null) {
			textControl.setToolTipText(val);
		}
	}

	private void initColors(Text textControl) {
		defaultForeground = textControl.getForeground();
		ColorRegistry colorRegistry = JFaceResources.getColorRegistry();
		disabledForeground = colorRegistry.get("DarkGray");
		if (disabledForeground == null) {
			if (!colorRegistry.hasValueFor("DarkGray")) {
				colorRegistry.put("DarkGray", new RGB(0x69, 0x69, 0x69));
			}
			disabledForeground = colorRegistry.get("DarkGray");
		}
	}

	private void updateTextFieldColor() {
		Text textControl = getTextControl();
		if (textControl == null) {
			return;
		}
		Color color = (this.override) ? defaultForeground : disabledForeground;
		textControl.setForeground(color);
	}

	@Override
	protected boolean checkState() {
		Text textControl = getTextControl();
		if (textControl == null) {
			return false;
		}

		String textStr = textControl.getText();
		if (textStr.toUpperCase().startsWith("AUTO")) {
			return true;
		} else if ("".equals(textStr)) {
			return true;
		}
		return super.checkState();
	}

	@Override
	protected void doLoad() {
		this.override = getPreferenceStore().getBoolean(overridePrefName);
		String str;
		if (override) {
			str = "" + getPreferenceStore().getInt(getPreferenceName());
		} else {
			str = getAutoValueForText();
		}
		setText(str);
		oldValue = str; 
	}

	@Override
	protected void doLoadDefault() {
		this.override = getPreferenceStore().getDefaultBoolean(overridePrefName);
		String str;
		if (override) {
			str = "" + getPreferenceStore().getDefaultInt(getPreferenceName());
		} else {
			str = getAutoValueForText();
		}
		setText(str);
		valueChanged();
	}

	@Override
	protected void doStore() {
		Text textControl = getTextControl();
		if (textControl != null) {
			if (override) {
				Integer val = Integer.valueOf(textControl.getText());
				getPreferenceStore().setValue(getPreferenceName(), val);
				getPreferenceStore().setValue(overridePrefName, true);
			} else {
				getPreferenceStore().setValue(overridePrefName, false);
				getPreferenceStore().setToDefault(getPreferenceName());
			}
		}
	}
	
	@NonNull
	private String getAutoValueForText() {
		if (autoTextValue != null && !autoTextValue.isEmpty()) {
			return "AUTO (" + autoTextValue + ")";
		} else {
			return "AUTO";
		}
	}
	
	public void setAutoValue(String autoValue) {
		if (autoValue != null && !autoValue.equals(this.autoTextValue)) {
			this.autoTextValue = autoValue;
			int autoValueLen = getAutoValueForText().length();
			if (autoValueLen > DEFAULT_TEXT_LIMIT) {
				setTextLimit(autoValueLen); // increase text limit otherwise it gets truncated
			}
			if (!override) { // update text control
				String str = getAutoValueForText();
				Text textControl = getTextControl();
				if (textControl != null) {
					textControl.setText(str);
				}
			}
		}
	}
	
	public String getAutoValue() {
		return this.autoTextValue;
	}
	
	/**
	 * @param str new text to display, if null, then ({@link #getAutoValueForText()} will be used 
	 * @return true if able to set new text on text control, otherwise false
	 * @noreference This method is not intended to be referenced by clients.
	 */
	public boolean setText(String str) {
		Text textControl = getTextControl();
		if (textControl != null) {
			if (str == null) {
				str = getAutoValueForText();
			}
			textControl.setText(str);
			return true;
		}
		return false;
	}
}
