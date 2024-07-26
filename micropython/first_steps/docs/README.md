# README

## Descrição do Vídeo
Este vídeo tutorial ensina como instalar o MicroPython no módulo ESP32 e executar um exemplo básico de 'Hello World' usando o software PuTTY. É um guia passo a passo para iniciantes que desejam configurar e começar a programar com o ESP32 utilizando MicroPython.

## Conteúdo do Vídeo
- **Introdução ao MicroPython e ESP32:** Breve explicação sobre o que é MicroPython e suas vantagens para o desenvolvimento com ESP32.
- **Preparação do Ambiente:** Lista de ferramentas e software necessários, incluindo o ESP32, cabo USB, PuTTY, e firmware do MicroPython.
- **Instalação do Firmware MicroPython no ESP32:** Passos detalhados para baixar e instalar o firmware do MicroPython no ESP32.
- **Configuração do PuTTY:** Instruções para configurar e utilizar o PuTTY para se comunicar com o ESP32.
- **Executando o 'Hello World':** Exemplo prático de código para testar a instalação do MicroPython e verificar se tudo está funcionando corretamente.

## Requisitos
- Módulo ESP32
- Cabo USB
- Firmware do MicroPython
- Software PuTTY
- Driver USB para ESP32 (CP2102 ou CH340, dependendo do modelo do ESP32)

## Passo a Passo

### 1. Preparar o Ambiente
- **Ferramentas Necessárias:**
  - Módulo ESP32
  - Cabo USB
  - Firmware do MicroPython
  - Software PuTTY
  - Driver USB para ESP32

### 2. Baixar e Instalar o Firmware do MicroPython
- Baixe a versão mais recente do firmware do MicroPython para ESP32 do site oficial.
- Utilize uma ferramenta como `esptool.py` para instalar o firmware no ESP32.

### 3. Configurar o PuTTY
- Baixe e instale o PuTTY.
- Configure o PuTTY para se comunicar com o ESP32 através da porta serial correta.
  - **Configurações Principais:**
    - Tipo de conexão: Serial
    - Porta Serial: COMx (substitua 'x' pelo número da porta correta)
    - Velocidade: 115200

### 4. Executar o Exemplo 'Hello World'
- Conecte o ESP32 ao computador e abra o PuTTY.
- No terminal do PuTTY, execute os seguintes comandos em MicroPython:

```python
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(not led.value())
    time.sleep(1)
```

- Este código faz com que o LED embutido no ESP32 pisque a cada segundo, confirmando que o MicroPython está funcionando corretamente.

## Recursos Adicionais
- [Documentação Oficial do MicroPython](https://docs.micropython.org/en/latest/esp32/)
- [Download do Firmware MicroPython](https://micropython.org/download/esp32/)
- [Download do PuTTY](https://www.putty.org/)

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

---

Sinta-se à vontade para adaptar este README conforme necessário para atender às suas necessidades específicas e incluir quaisquer outras informações que você ache relevantes.
