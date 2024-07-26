import network  # Importa o módulo network para permitir a configuração de interfaces de rede.
import time  # Importa o módulo time para usar funções relacionadas ao tempo, como sleep.

# Cria um objeto WLAN para a interface STA (Station), permitindo que o ESP32 se conecte a uma rede Wi-Fi.
sta_if = network.WLAN(network.STA_IF)

# Ativa a interface STA e se conecta à rede Wi-Fi com SSID 'rede' e senha 'senha1234'.
sta_if.active(True)  # Ativa a interface Wi-Fi.
sta_if.connect('rede', 'senha1234')  # Conecta à rede Wi-Fi com o SSID e senha fornecidos.

# Loop que verifica se a conexão foi estabelecida. Enquanto não estiver conectado, imprime "Conectando..." e aguarda 1 segundo.
while not sta_if.isconnected():
    print("Conectando...")
    time.sleep(1)

# Uma vez conectado, imprime 'Conectado!'.
print('Conectado!')

# Imprime as configurações de rede atuais (como IP, máscara de sub-rede, gateway, etc.) da interface STA.
print('Configurações de rede: ' + str(sta_if.ifconfig()))
