from selfdrive.car import dbc_dict

class CAR:
  PRIUS = "TOYOTA PRIUS 2017"
  RAV4H = "TOYOTA RAV4 2017 HYBRID"
  RAV4 = "TOYOTA RAV4 2017"
  COROLLA = "TOYOTA COROLLA 2017"
  LEXUS_RXH = "LEXUS RX HYBRID 2017"


class ECU:
  CAM = 0 # camera
  DSU = 1 # driving support unit
  APGS = 2 # advanced parking guidance system


# addr: (ecu, cars, bus, 1/freq*100, vl)
STATIC_MSGS = [(0x141, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   2, '\x00\x00\x00\x46'),
               (0x128, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   3, '\xf4\x01\x90\x83\x00\x37'),

               (0x292, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0,   3, '\x00\x00\x00\x00\x00\x00\x00\x9e'),
               (0x283, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0,   3, '\x00\x00\x00\x00\x00\x00\x8c'),
               (0x2E6, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, '\xff\xf8\x00\x08\x7f\xe0\x00\x4e'),
               (0x2E7, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, '\xa8\x9c\x31\x9c\x00\x00\x00\x02'),

               (0x240, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
               (0x241, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
               (0x244, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
               (0x245, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
               (0x248, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   5, '\x00\x00\x00\x00\x00\x00\x01'),
               (0x344, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0,   5, '\x00\x00\x01\x00\x00\x00\x00\x50'),

               (0x160, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   7, '\x00\x00\x08\x12\x01\x31\x9c\x51'),
               (0x161, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   7, '\x00\x1e\x00\x00\x00\x80\x07'),

               (0x32E, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0,  20, '\x00\x00\x00\x00\x00\x00\x00\x00'),
               (0x33E, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,  20, '\x0f\xff\x26\x40\x00\x1f\x00'),
               (0x365, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,  20, '\x00\x00\x00\x80\x03\x00\x08'),
               (0x365, ECU.DSU, (CAR.RAV4, CAR.COROLLA), 0,  20, '\x00\x00\x00\x80\xfc\x00\x08'),
               (0x366, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,  20, '\x00\x00\x4d\x82\x40\x02\x00'),
               (0x366, ECU.DSU, (CAR.RAV4, CAR.COROLLA), 0,  20, '\x00\x72\x07\xff\x09\xfe\x00'),

               (0x367, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0,  40, '\x06\x00'),

               (0x414, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x00\x00\x00\x00\x00\x00\x17\x00'),
               (0x489, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
               (0x48a, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
               (0x48b, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x66\x06\x08\x0a\x02\x00\x00\x00'),
               (0x4d3, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x1C\x00\x00\x01\x00\x00\x00\x00'),
               (0x130, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1, 100, '\x00\x00\x00\x00\x00\x00\x38'),
               (0x466, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4), 1, 100, '\x20\x20\xAD'),
               (0x466, ECU.CAM, (CAR.COROLLA), 1, 100, '\x24\x20\xB1'),
               (0x396, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\xBD\x00\x00\x00\x60\x0F\x02\x00'),
               (0x43A, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x84\x00\x00\x00\x00\x00\x00\x00'),
               (0x43B, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x00\x00\x00\x00\x00\x00\x00\x00'),
               (0x497, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x00\x00\x00\x00\x00\x00\x00\x00'),
               (0x4CC, ECU.APGS, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x0D\x00\x00\x00\x00\x00\x00\x00'),
               (0x4CB, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x0c\x00\x00\x00\x00\x00\x00\x00'),
               (0x470, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 1, 100, '\x00\x00\x02\x7a'),
              ]


def check_ecu_msgs(fingerprint, candidate, ecu):
  # return True if fingerprint contains messages normally sent by a given ecu
  ecu_msgs = [x[0] for x in STATIC_MSGS if (x[1] == ecu and
                                            candidate in x[2] and
                                            x[3] == 0)]

  return any(msg for msg in fingerprint if msg in ecu_msgs)


FINGERPRINTS = {
  CAR.RAV4: [{
    36L: 8, 37L: 8, 170L: 8, 180L: 8, 186L: 4, 426L: 6, 452L: 8, 464L: 8, 466L: 8, 467L: 8, 547L: 8, 548L: 8, 552L: 4, 562L: 4, 608L: 8, 610L: 5, 643L: 7, 705L: 8, 725L: 2, 740L: 5, 800L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 871L: 2, 896L: 8, 897L: 8, 900L: 6, 902L: 6, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 951L: 8, 955L: 4, 956L: 8, 979L: 2, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1008L: 2, 1014L: 8, 1017L: 8, 1041L: 8, 1042L: 8, 1043L: 8, 1044L: 8, 1056L: 8, 1059L: 1, 1114L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 1196L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1263L: 8, 1264L: 8, 1279L: 8, 1408L: 8, 1409L: 8, 1410L: 8, 1552L: 8, 1553L: 8, 1554L: 8, 1555L: 8, 1556L: 8, 1557L: 8, 1561L: 8, 1562L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1584L: 8, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1596L: 8, 1597L: 8, 1600L: 8, 1656L: 8, 1664L: 8, 1728L: 8, 1745L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  }],
  CAR.RAV4H: [{
    36L: 8, 37L: 8, 170L: 8, 180L: 8, 186L: 4, 296L: 8, 426L: 6, 452L: 8, 464L: 8, 466L: 8, 467L: 8, 547L: 8, 548L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 4, 581L: 5, 608L: 8, 610L: 5, 643L: 7, 705L: 8, 713L: 8, 725L: 2, 740L: 5, 800L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 871L: 2, 896L: 8, 897L: 8, 900L: 6, 902L: 6, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 3, 955L: 8, 956L: 8, 979L: 2, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1008L: 2, 1014L: 8, 1017L: 8, 1041L: 8, 1042L: 8, 1043L: 8, 1044L: 8, 1056L: 8, 1059L: 1, 1114L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1184L: 8, 1185L: 8, 1186L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 1196L: 8, 1197L: 8, 1198L: 8, 1199L: 8, 1212L: 8, 1227L: 8, 1228L: 8, 1232L: 8, 1235L: 8, 1237L: 8, 1263L: 8, 1264L: 8, 1279L: 8, 1408L: 8, 1409L: 8, 1410L: 8, 1552L: 8, 1553L: 8, 1554L: 8, 1555L: 8, 1556L: 8, 1557L: 8, 1561L: 8, 1562L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1584L: 8, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1596L: 8, 1597L: 8, 1600L: 8, 1656L: 8, 1664L: 8, 1728L: 8, 1745L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
 }],
  CAR.PRIUS: [{
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 863L: 8, 869L: 7, 870L: 7, 871L: 2, 898L: 8, 900L: 6, 902L: 6, 905L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  # Prius Prime
  {
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 824L: 2, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 863L: 8, 869L: 7, 870L: 7, 871L: 2,898L: 8, 900L: 6, 902L: 6, 905L: 8, 913L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 974L: 8, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1076L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1164L: 8, 1165L: 8, 1166L: 8, 1167L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  # Taiwanese Prius Prime
  {
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 824L: 2, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 845L: 5, 863L: 8, 869L: 7, 870L: 7, 871L: 2,898L: 8, 900L: 6, 902L: 6, 905L: 8, 913L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 974L: 8, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1076L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1164L: 8, 1165L: 8, 1166L: 8, 1167L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1264L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  }],
  CAR.COROLLA: [{
    36: 8, 37: 8, 170: 8, 180: 8, 186: 4, 426: 6, 452: 8, 464: 8, 466: 8, 467: 8, 547: 8, 548: 8, 552: 4, 608: 8, 610: 5, 643: 7, 705: 8, 740: 5, 800: 8, 835: 8, 836: 8, 849: 4, 869: 7, 870: 7, 871: 2, 896: 8, 897: 8, 900: 6, 902: 6, 905: 8, 911: 8, 916: 2, 921: 8, 933: 8, 944: 8, 945: 8, 951: 8, 955: 4, 956: 8, 979: 2, 992: 8, 998: 5, 999: 7, 1000: 8, 1001: 8, 1017: 8, 1041: 8, 1042: 8, 1043: 8, 1044: 8, 1056: 8, 1059: 1, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1196: 8, 1227: 8, 1235: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1561: 8, 1562: 8, 1568: 8, 1569: 8, 1570: 8, 1571: 8, 1572: 8, 1584: 8, 1589: 8, 1592: 8, 1596: 8, 1597: 8, 1600: 8, 1664: 8, 1728: 8, 1779: 8, 1904: 8, 1912: 8, 1990: 8, 1998: 8
  },
  # Corolla LE 2017
  {
    36: 8, 37: 8, 170: 8, 180: 8, 186: 4, 426: 6, 452: 8, 464: 8, 466: 8, 467: 8, 547: 8, 548: 8, 552: 4, 608: 8, 610: 5, 643: 7, 705: 8, 740: 5, 800: 8, 835: 8, 836: 8, 849: 4, 869: 7, 870: 7, 871: 2, 896: 8, 897: 8, 900: 6, 902: 6, 905: 8, 911: 8, 916: 2, 921: 8, 933: 8, 944: 8, 945: 8, 951: 8, 955: 4, 956: 8, 979: 2, 998: 5, 999: 7, 1000: 8, 1001: 8, 1017: 8, 1041: 8, 1042: 8, 1043: 8, 1044: 8, 1056: 8, 1059: 1, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1196: 8, 1227: 8, 1235: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1561: 8, 1562: 8, 1568: 8, 1569: 8, 1570: 8, 1571: 8, 1572: 8, 1592: 8, 1596: 8, 1597: 8, 1600: 8, 1664: 8, 1779: 8, 1904: 8, 1912: 8, 1990: 8, 1998: 8, 2016: 8, 2017: 8, 2018: 8, 2019: 8, 2020: 8, 2021: 8, 2022: 8, 2023: 8, 2024: 8
  }],
  CAR.LEXUS_RXH: [{
    36: 8, 37: 8, 166: 8, 170: 8, 180: 8, 295: 8, 296: 8, 426: 6, 452: 8, 466: 8, 467: 8, 550: 8, 552: 4, 560: 7, 562: 6, 581: 5, 608: 8, 610: 5, 643: 7, 658: 8, 713: 8, 740: 5, 742: 8, 743: 8, 800: 8, 810: 2, 812: 3, 814: 8, 830: 7, 835: 8, 836: 8, 845: 5, 863: 8, 869: 7, 870: 7, 871: 2, 898: 8, 900: 6, 902: 6, 905: 8, 913: 8, 918: 8, 921: 8, 933: 8, 944: 8, 945: 8, 950: 8, 951: 8, 953: 8, 955: 8, 956: 8, 971: 7, 975: 6, 993: 8, 998: 5, 999: 7, 1000: 8, 1001: 8, 1005: 2, 1014: 8, 1017: 8, 1020: 8, 1041: 8, 1042: 8, 1044: 8, 1056: 8, 1059: 1, 1063: 8, 1071: 8, 1077: 8, 1082: 8, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1164: 8, 1165: 8, 1166: 8, 1167: 8, 1227: 8, 1228: 8, 1235: 8, 1237: 8, 1264: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1568: 8, 1570: 8, 1571: 8, 1572: 8, 1575: 8, 1595: 8, 1777: 8, 1779: 8, 1808: 8, 1810: 8, 1816: 8, 1818: 8, 1840: 8, 1848: 8, 1904: 8, 1912: 8, 1940: 8, 1941: 8, 1948: 8, 1949: 8, 1952: 8, 1956: 8, 1960: 8, 1964: 8, 1986: 8, 1990: 8, 1994: 8, 1998: 8, 2004: 8, 2012: 8
  }],
}


DBC = {
  CAR.RAV4H: dbc_dict('toyota_rav4_hybrid_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.RAV4: dbc_dict('toyota_rav4_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.PRIUS: dbc_dict('toyota_prius_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.COROLLA: dbc_dict('toyota_corolla_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.LEXUS_RXH: dbc_dict('lexus_rx_hybrid_2017_pt_generated', 'toyota_prius_2017_adas'),
}
