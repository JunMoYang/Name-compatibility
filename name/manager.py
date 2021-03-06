import operator
import unicodedata


# "names"는 'name'의 '유효성 검사'및 '필요한 기능'들이 포함됩니다.
class names:
    def __init__(self, name1, name2):
        self.__name1 = name1
        self.__name2 = name2

    # 'name1'과 'name2'의 이름을 번갈아 가면서 'name'에 기입합니다.
    # 'name1[0]', 'name2[0]', 'name1[1]', 'name2[1]' ...
    def mixNames(self):
        name = {}
        if self.__verification():
            for i in range(3):
                if i != 0:
                    name[i + i] = self.__name1[i]
                else:
                    name[i] = self.__name1[i]
            for i in range(3):
                if i == 0:
                    name[i + 1] = self.__name2[i]
                else:
                    name[i + i + 1] = self.__name2[i]

            sortedNames = sorted(name.items(), key=operator.itemgetter(0))
            result = list()
            for i in range(len(sortedNames)):
                result.append(sortedNames[i][1])
            return result
        else:
            return False

    # 'type', '길이', '언어'를 체크.
    def __verification(self):
        if not self.__isString(self.__name1) or not self.__isString(self.__name2):
            return False
        elif not self.__checkLen(self.__name1) or not self.__checkLen(self.__name2):
            return False
        else:
            return True

    def __isString(self, name):
        if type(name) == str:
            return True
        else:
            print("Error Type : ", name)
            return False

    def __checkLen(self, name):
        if len(name) == 3:
            return True
        else:
            print("Error Length : ", name)
            return False
