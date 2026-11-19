from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import DictProperty, NumericProperty, StringProperty
from quick_order import MENU, Basket

class QuickOrderApp(App):
    counts = DictProperty()
    total = NumericProperty(0)
    summary = StringProperty("Basket is empty")

    def build(self):
        self.title = "ShopEasy quick order"
        self.basket = Basket()
        self.counts = dict(self.basket.qty)
        root = Builder.load_file("quickorder.kv")
        for name in MENU:
            root.ids.rows.add_widget(Factory.ProductRow(name=name))
        return root

    def change(self, name, step):
        self.basket.add(name, step)
        self.counts = dict(self.basket.qty)
        self.total = self.basket.total()
        self.summary = self.basket.summary()

if __name__ == "__main__":
    QuickOrderApp().run()