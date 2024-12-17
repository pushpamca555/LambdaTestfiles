from Pages.BasePage import BasePage
from Pages.InputForms import InputForms
from Tests.common_tests import CommonTests
from Utilities.test_data import TestData


class TestScenario3(CommonTests):
    def test_form_inputs(self):
        base_page = BasePage(self.driver)
        input_forms_page = InputForms(self.driver)

        # Click “Simple Form Demo” under Input Forms.
        base_page.click_on_element(TestData.input_form_submit_link)

        # Click submit without entering input field values
        base_page.click_on_element(TestData.form_submit_button)

        
        # input_forms_page.validate_warning_message_for_input_fields()

        # Enter form details
        input_forms_page.enter_form_details()

        # Click on Submit
        base_page.click_on_element(TestData.form_submit_button)





