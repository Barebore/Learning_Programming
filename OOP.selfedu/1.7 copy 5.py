class GenerationIP:
    ip = -1
    staticmethod
    def generatorIP():
        GenerationIP.ip += 1
        return GenerationIP.ip
        
class Server:
    def __init__(self):
        self.ip = GenerationIP.generatorIP()
        self.buffer = []

    @staticmethod
    def send_data(data):
        Router.buffer.append(data)
    
    def get_data(self):
        a = self.buffer
        self.buffer = []
        return a
    
    def get_ip(self):
        return self.ip
    
class Router:
    buffer = []
    server = []
    
    def link(self, server):
        self.server.append(server)
    
    def unlink(self, server):
        del self.server[self.server.index(server)]
        
    def send_data(self):
        for i in self.buffer:
            for j in range(len(self.server)):
               # print(cls.server[j].get_ip, i.ip)
                #print(j)
                if self.server[j].ip == i.ip:
                    #print(self.server[j],self.server[j].ip, i.ip, i.data, self.server[j].buffer)
                    self.server[j].buffer.append(i)
                    #print(self.server[j], self.server[j].buffer)
                    #print(self.server[j].buffer)
                    #cls.server[j].buffer = []          
        self.buffer = []
            
        
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"
router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"