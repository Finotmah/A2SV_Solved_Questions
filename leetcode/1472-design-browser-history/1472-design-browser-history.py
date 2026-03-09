class Dl_node:
    def __init__(self, url):
        self.url = url
        self.pre = None
        self.next =  None
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = Dl_node(homepage)
        self.curr.next = None

    def visit(self, url):
        new_n = Dl_node(url)
        self.curr.next = new_n
        new_n.pre = self.curr
        self.curr = new_n
        
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.curr.pre:
            self.curr = self.curr.pre
            steps -= 1
        return self.curr.url
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)