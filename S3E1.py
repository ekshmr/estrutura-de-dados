temp_media_mes: list[float] = []
mes: int = 1
float_temp: float = float()
qual_temperatura: str = str(input("Digite qual formato de temperatura será usado (°F/°C) "))
qual_pais: str = str(input("Digite de qual país é a temperatura "))
media_anual: float = 0
while mes < 13:
    if mes < 10:
        float_temp = float(input(f"Digite a temperatura média de 0{mes}/2021: "))
    elif mes > 9:
        float_temp = float(input(f"Digite a temperatura média de {mes}/2021: "))
    temp_media_mes.append(float_temp)
    media_anual += temp_media_mes[mes-1]
    mes += 1
    
media_anual = round(media_anual / 12, 1)

print(f"Média anual {media_anual}")
janeiro = temp_media_mes[0]
fevereiro = temp_media_mes[1]
marco = temp_media_mes[2]
abril = temp_media_mes[3]
maio = temp_media_mes[4]
junho = temp_media_mes[5]
julho = temp_media_mes[6]
agosto = temp_media_mes[7]
setembro = temp_media_mes[8]
outubro = temp_media_mes[9]
novembro = temp_media_mes[10]
dezembro = temp_media_mes[11]
print(f"Média mensal\n01/2022 {janeiro}°{qual_temperatura}\n02/2022 {fevereiro}°{qual_temperatura}\n03/2022 {marco}°{qual_temperatura}\n04/2022 {abril}°{qual_temperatura}\n05/2022 {maio}°{qual_temperatura}\n06/2022 {junho}°{qual_temperatura}\n07/2022 {julho}°{qual_temperatura}\n08/2022 {agosto}°{qual_temperatura}\n09/2022 {setembro}°{qual_temperatura}\n10/2022 {outubro}°{qual_temperatura}\n11/2022 {novembro}°{qual_temperatura}\n12/2022 {dezembro}°{qual_temperatura}")

