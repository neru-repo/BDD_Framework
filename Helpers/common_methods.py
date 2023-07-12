from Logs import logs_file


log = logs_file.get_logs()


class CommonMethods:

    @staticmethod
    def find_element(driver, locator):
        return driver.find_element(list(locator.keys())[0], list(locator.values())[0])

    @staticmethod
    def send_keys(element, text):
        log.info(f"Entered text is {text} in locator: {element}")
        element.send_keys(text)

    def click(self, driver, locator):
        element = self.find_element(driver, locator)
        log.info("Submit button clicked")
        element.click()

    def get_text(self, driver, locator):
        element = self.find_element(driver, locator)
        log.info(element)
        log.info(f"The text obtained is {element.text}")
        return element.text

    def clear_text(self, driver, locator):
        element = self.find_element(driver, locator)
        element.clear()

