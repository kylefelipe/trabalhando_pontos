from collections import namedtuple
from typing import NamedTuple
from operator import itemgetter, attrgetter
from qgis.core import (QgsGeometry, QgsPoint, QgsLineString, QgsProject)


csv = (
    (6117005.0314023457467556, 9998299.13320730440318584, 23),
    (5957803.89960606396198273, 10050685.83042232133448124, 20),
    (5976853.60768425092101097, 10009865.02739763259887695, 21),
    (5908818.93597643822431564, 10033677.16249536722898483, 18),
    (5921745.52360092289745808, 10086744.20642746239900589, 19),
    (6108160.52408033050596714, 10005782.94709516316652298, 16),
    (5919704.48344968818128109, 9970404.91780710220336914, 17),
    (6163268.60816365852952003, 9962921.10391924157738686, 30),
    (6091832.2028704546391964, 9935026.88851903937757015, 31),
    (6172113.11548567470163107, 10097629.75390071235597134, 28),
    (6187761.08997847139835358, 10018709.53471964783966541, 29),
    (6006788.86323568876832724, 10090145.94001285172998905, 26),
    (6046248.97282622009515762, 10113958.07511058636009693, 27),
    (6028559.95818218868225813, 10015988.14785133674740791, 24),
    (6005428.16980153229087591, 10044562.70996861718595028, 25),
    (5980935.68798672035336494, 9927543.07463117875158787, 38),
    (5973451.87409886065870523, 9964962.14407047629356384, 39),
    (6038084.81222128309309483, 10006463.29381224140524864, 36),
    (6031961.69176757987588644, 9943871.39584105461835861, 37),
    (6115644.33796818926930428, 10092867.3268811646848917, 34),
    (6056454.17358239274471998, 10045923.4034027736634016, 35),
    (6078905.61524597089737654, 10020750.5748708825558424, 32),
    (6108840.8707974087446928, 10082662.12612499296665192, 33),
    (5933311.41779125109314919, 9952715.90316306985914707, 46),
    (5957803.89960606396198273, 9876517.07085032016038895, 47),
    (5902015.4688056567683816, 9927543.07463117875158787, 44),
    (5929909.68420585989952087, 9947953.47614352405071259, 45),
    (6018354.75742601696401834, 9897607.81907974183559418, 42),
    (5943516.61854742281138897, 9878558.11100155487656593, 43),
    (5990460.54202581383287907, 9979929.77184619568288326, 40),
    (6010870.94353815726935863, 9943871.39584105461835861, 41),
    (5933991.76450832933187485, 9921419.95417747646570206, 54),
    (5931270.3776400163769722, 9901689.899382209405303, 55),
    (5887047.84102993831038475, 9905091.63296760059893131, 52),
    (5919704.48344968818128109, 9919378.91402624174952507, 53),
    (5928548.99077170435339212, 9894886.43221142888069153, 50),
    (5902695.81552273500710726, 9883320.53802110068500042, 51),
    (5976173.26096717268228531, 9909173.71327007003128529, 48),
    (5951680.77915236074477434, 9918698.56730916351079941, 49),
    (5896572.69506903178989887, 10009184.68068055436015129, 62),
    (5868678.47966882865875959, 10037759.24279783666133881, 63),
    (5872760.55997129715979099, 9983331.50543158501386642, 60),
    (5891129.92133240681141615, 10005102.60037808679044247, 61),
    (5883646.10744454711675644, 9935026.88851903937757015, 58),
    (5865957.09280051570385695, 9951355.20972891338169575, 59),
    (5914261.70971306320279837, 9908493.36655299179255962, 56),
    (5895892.34835195355117321, 9912575.4468554612249136, 57),
    (5835341.49053200054913759, 9939108.96882150694727898, 70),
    (5844185.99785401578992605, 9918698.56730916351079941, 71),
    (5861194.66578096896409988, 10002381.21350977383553982, 68),
    (5874801.60012253187596798, 10033677.16249536722898483, 69),
    (5815611.43573673442006111, 9957478.33018261753022671, 66),
    (5821734.5561904376372695, 9932985.84836780466139317, 67),
    (5860514.31906389072537422, 10044562.70996861718595028, 64),
    (5820373.86275628115981817, 9993536.70618775859475136, 65),
    (5959844.93975729774683714, 9918698.56730916351079941, 78),
    (5973451.87409886065870523, 9898968.5125138983130455, 79),
    (5920384.83016676642000675, 9894886.43221142888069153, 76),
    (5920384.83016676642000675, 9898288.16579682007431984, 77),
    (5920384.83016676642000675, 9858828.05620628781616688, 74),
    (5941475.57839618809521198, 9866311.87009414844214916, 75),
    (5870719.51982006337493658, 9893525.7387772724032402, 72),
    (5885006.80087870359420776, 9869713.60367953777313232, 73),
    (6233344.32002270594239235, 9890804.35190895944833755, 86),
    (6391184.75838483218103647, 9947273.12942644581198692, 87),
    (6413636.20004841033369303, 9924141.34104578942060471, 84),
    (6328592.86041364446282387, 9996258.09305606968700886, 85),
    (6140136.81978300213813782, 9903050.59281636588275433, 82),
    (6234705.01345686241984367, 9891484.69862603768706322, 83),
    (6006788.86323568876832724, 9872434.99054785072803497, 80),
    (6095914.28317292407155037, 9884000.88473817892372608, 81),
    (6377577.82404326926916838, 10109195.64809104055166245, 94),
    (6370774.35687248781323433, 10037759.24279783666133881, 95),
    (6259877.8419887525960803, 10088785.24657869525253773, 92),
    (6251713.68138381559401751, 10088785.24657869525253773, 93),
    (6245590.56093011237680912, 9996938.43977314792573452, 90),
    (6260558.18870583083480597, 10004422.2536610085517168, 91),
    (6274845.46976447198539972, 9917337.87387500703334808, 88),
    (6212933.91851036250591278, 9949314.16957767866551876, 89),
    (6090471.50943629909306765, 9974486.99810956977307796, 102),
    (6204769.75790542457252741, 10038439.58951491490006447, 103),
    (6014953.02384062670171261, 9973806.6513924915343523, 100),
    (6070741.45464103296399117, 9905091.63296760059893131, 101),
    (6002706.78293322026729584, 10005782.94709516316652298, 98),
    (5999305.04934782907366753, 9998299.13320730440318584, 99),
    (6261238.53542290907353163, 9995577.7463389914482832, 96),
    (6148300.98038794007152319, 10003061.56022685207426548, 97),
    (6382340.25106281600892544, 9866311.87009414844214916, 110),
    (6324510.78011117503046989, 9920059.26074331998825073, 111),
    (6307502.11218422185629606, 9902370.24609928764402866, 108),
    (6383020.5977798942476511, 9883320.53802110068500042, 109),
    (6263279.57557414378970861, 9941150.00897274166345596, 106),
    (6277566.8566327840089798, 9916657.52715792879462242, 107),
    (6268722.34931076876819134, 10009865.02739763259887695, 104),
    (6275525.81648155022412539, 9975847.69154372625052929, 105),
    (6204089.41118834633380175, 10051366.1771393995732069, 118),
    (6217015.99881283100694418, 10085383.51299330592155457, 119),
    (6306821.7654671436175704, 10028234.38875874318182468, 116),
    (6279607.89678401872515678, 10040480.62966614961624146, 117),
    (6323830.43339409679174423, 10109195.64809104055166245, 114),
    (6317026.96622331626713276, 10075858.65895421057939529, 115),
    (6342880.14147228468209505, 9999659.82664146088063717, 112),
    (6323150.08667701855301857, 10098310.100617790594697, 113),
    (6129931.61902683041989803, 10078580.04582252353429794, 126),
    (6164629.30159781500697136, 10147975.4109644927084446, 127),
    (6102717.75034370552748442, 10040480.62966614961624146, 124),
    (6104758.79049493931233883, 10041160.97638322599232197, 125),
    (6069380.76120687648653984, 10040480.62966614961624146, 122),
    (6087750.122567986138165, 10071776.57865174300968647, 123),
    (6142177.8599342368543148, 10048644.79027108661830425, 120),
    (6136735.08619761187583208, 10043202.01653446070849895, 121),
    (5970050.14051346946507692, 10093547.67359824292361736, 132),
    (6034002.73191881366074085, 10073137.27208589948713779, 130),
    (6012231.63697231374680996, 10106474.2612227275967598, 131),
    (6096594.62989000231027603, 10118040.1554130557924509, 128),
    (6080946.65539720468223095, 10095588.71374947763979435, 129),
    (5956443.2061719074845314, 10083342.47284207120537758, 6),
    (5933991.76450832933187485, 10109195.64809104055166245, 7),
    (6053052.43999700155109167, 10072456.92536882124841213, 4),
    (5970730.48723054770380259, 10049325.13698816485702991, 5),
    (5948959.39228404778987169, 9994897.39962191320955753, 2),
    (6016994.06399186048656702, 10064292.76476388238370419, 3),
    (5904056.50895689148455858, 10028914.73547582142055035, 1),
    (6016994.06399186048656702, 10069735.53850050829350948, 14),
    (6073462.84150934591889381, 10038439.58951491490006447, 15),
    (5953041.47258651629090309, 10099670.79405194520950317, 12),
    (5882285.41401039157062769, 10078580.04582252353429794, 13),
    (5906777.89582520350813866, 9959519.37033385038375854, 10),
    (5963927.02005976717919111, 10094228.02031532116234303, 11),
    (5883646.10744454711675644, 10079260.39253960177302361, 8),
    (5940795.2316791107878089, 10026873.69532458670437336, 9),
    (6051011.39984576776623726, 9959519.37033385038375854, 22),
)

Ponto = namedtuple('Ponto', [('id', int)])

campos = [('geometria', QgsPoint), ('id', int)]
ConjuntoPontos = NamedTuple('ConjuntoPontos', [campo for campo in campos])
# class ConjuntoPontos(NamedTuple):
#     geometria: Point
#     fid: int
#     for

camada = [(id, QgsPoint(x, y)}]
pontos = [(QgsPoint(x, y), id) for x, y, id in csv]

pts = [ConjuntoPontos(p, id) for p, id in pontos]

field_to_order_by = ['x']
order_by = attrgetter(*field_to_order_by)
order_by = None
ordered = sorted(pontos, key=order_by, reverse=)
del(ordered)
print(pontos.sort(reverse=True))
ordered[:10]
