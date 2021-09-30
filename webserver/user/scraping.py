from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SiaConnection:

    def __init__(self, username, password) -> None:
        # SIA index workaround
        self.index = 1
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.username = username
        self.password = password
        self.authenticate()

    def authenticate(self) -> None:
        self.driver.get("https://sia.unal.edu.co/ServiciosApp")
        if "Portal académico - Universidad Nacional de Colombia" == self.driver.title:
            usernameField = self.driver.find_element_by_xpath(
                '//*[@id="username"]')
            usernameField.clear()
            usernameField.send_keys(self.username)
            passwordField = self.driver.find_element_by_xpath(
                '//*[@id="password"]')
            passwordField.clear()
            passwordField.send_keys(self.password)
            self.driver.find_elements_by_css_selector(
                ".btn[type='submit']")[0].click()

    def getUserDataAndCreateUser(self) -> dict:
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            '//*[@id="pt1:men-portlets:sdi::head"]')).click()
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath('//*[@id="pt1:men-portlets:sni"]')).click()
        userData = {
            'fullname': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot4::content"]')).text,
            'document': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot1::content"]')).text,
            'expeditionOfDocumentDepartment': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot7::content"]')).text,
            'expeditionOfDocumentPlace': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot8::content"]')).text,
            'sex': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot6::content"]')).text,
            'etnicity': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot10::content"]')).text,
            'email': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot75::content"]')).text,
            'institutionalEmail': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot70::content"]')).text,
            'cellphoneNumber': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot12::content"]')).text,
            'phoneNumber': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot74::content"]')).text,
            'profileImage': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:i1"]')).get_attribute("src"),
            'birthDate': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:id1::content"]')).text,
            'birthPlace': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot13::content"]')).text,
            'nationality': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot17::content"]')).text,
            'bloodType': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot18::content"]')).text,
            'rhFactor': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot19::content"]')).text,
            'eps': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot20::content"]')).text,
            'direction': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:rte1::content"]/table/tbody/tr[1]/td')).text,
            'stratum': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot69::content"]')).text,
            'militarService': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot67::content"]')).text,
            'parents': [
                {
                    'name': ' '.join([x for x in [
                        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                            f'//*[@id="pt1:r1:{self.index}:ot30::content"]')).text,
                        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                            f'//*[@id="pt1:r1:{self.index}:ot31::content"]')).text,
                        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                            f'//*[@id="pt1:r1:{self.index}:ot33::content"]')).text,
                    ] if x != 'No informado']),
                    'typeOfDocument': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot37::content"]')).text,
                    'document': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot38::content"]')).text,
                },
                {'name': ' '.join([x for x in [
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                        f'//*[@id="pt1:r1:{self.index}:ot32::content"]')).text,
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                        f'//*[@id="pt1:r1:{self.index}:ot35::content"]')).text,
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                        f'//*[@id="pt1:r1:{self.index}:ot36::content"]')).text,
                ] if x != 'No informado']),
                    'typeOfDocument': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot39::content"]')).text,
                    'document': WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(f'//*[@id="pt1:r1:{self.index}:ot40::content"]')).text
                }
            ]
        }
        return userData

    def getGradesDataAndCreateGrades(self) -> list:
        self.index += 1
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            '//*[@id="pt1:men-portlets:j_idt1::head"]')).click()
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            '//*[@id="pt1:men-portlets:j_idt5"]')).click()
        gradesArray = list()
        semesters = WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_xpath(
            f'//*[@id="pt1:r1:{self.index}:soc1::content"]/option'))
        for semester in semesters:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
                f'//*[@id="pt1:r1:{self.index}:soc1::content"]')).click()
            semester.click()
            semesterGrades = {
                'semester': semester.text,
                'grades': []
            }
            try:
                for course in WebDriverWait(self.driver, 5).until(lambda x: x.find_elements_by_xpath(f'//*[@id="pt1:r1:{self.index}:i1:0:i2:0:pgl6"]/*[not(@style="display:none")]')):
                    courseParsed = course.text.replace(
                        ' APROBADA', '').replace(' REPROBADA', '').split('\n')
                    if len(courseParsed) == 2:
                        semesterGrades['grades'].append(
                            {'courseName': courseParsed[0], 'courseGrade': courseParsed[1], 'courseAprobed': 'APROBADA' in course.text})
            except TimeoutException:
                pass
            gradesArray.append(semesterGrades)
        return gradesArray

    def getSchedulesDataAndCreateSchedules(self):
        # TODO: Implement schedules (Has to be on hold because there's no test data)
        return

    def terminate(self) -> None:
        self.driver.close()
