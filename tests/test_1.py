from anatations.test_anatations import BaseAnatations
from time import sleep

class TestAllTests(BaseAnatations):


    # def test_swipe(self):
    #     self.base_page.swipe_too('MOVE_RIGHT')
    #     self.base_page.swipe_too('MOVE_UP', 3)
    #     self.base_page.swipe_too('MOVE_DOWN', 2)
    #     self.base_page.swipe_too('MOVE_LEFT')

    def test_2(self):
        # self.base_page.open_chrome()
        self.wildberries_app.open_and_add_localisation()

        sleep(10)



