class MediaCalculator:
    @staticmethod
    def calcular_media(list_numbers):
        result = 0
        for number in list_numbers:
            result += number
        return result / len(list_numbers)


print(
    MediaCalculator.calcular_media(
        [
            4,
            4,
            4,
            4,
            4,
        ]
    )
)
