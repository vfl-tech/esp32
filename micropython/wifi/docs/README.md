# README

## Descrição
Este script em Python é utilizado para conectar um módulo ESP32 a uma rede Wi-Fi. Ele utiliza o módulo `network` para configurar a interface de rede e o módulo `time` para controlar o tempo de espera durante o processo de conexão.

## Funcionalidades
- Ativa a interface de rede Wi-Fi do ESP32.
- Conecta-se a uma rede Wi-Fi utilizando o SSID e a senha fornecidos.
- Monitora o status da conexão, exibindo mensagens até que a conexão seja estabelecida.
- Exibe as configurações de rede uma vez que a conexão é bem-sucedida.

## Requisitos
- Módulo ESP32 com suporte a Wi-Fi.
- Ambiente de desenvolvimento configurado para ESP32 (ex: MicroPython).

## Uso
### Passos para executar o script:
1. **Importar Módulos Necessários:**
   O script utiliza os módulos `network` e `time`. Certifique-se de que eles estão disponíveis no ambiente MicroPython do seu ESP32.
   ```python
   import network
   import time
   ```

2. **Configurar a Interface Wi-Fi:**
   Crie um objeto `WLAN` para a interface `STA` (Station), que permite ao ESP32 se conectar a uma rede Wi-Fi.
   ```python
   sta_if = network.WLAN(network.STA_IF)
   ```

3. **Ativar a Interface e Conectar à Rede:**
   Ative a interface STA e conecte-se à rede Wi-Fi utilizando o SSID e a senha fornecidos.
   ```python
   sta_if.active(True)
   sta_if.connect('rede', 'senha1234')
   ```

4. **Monitorar a Conexão:**
   O script verifica continuamente se a conexão foi estabelecida, exibindo "Conectando..." enquanto a conexão não é realizada.
   ```python
   while not sta_if.isconnected():
       print("Conectando...")
       time.sleep(1)
   ```

5. **Exibir Informações de Conexão:**
   Uma vez conectado, o script imprime uma mensagem de sucesso e as configurações de rede atuais.
   ```python
   print('Conectado!')
   print('Configurações de rede: ' + str(sta_if.ifconfig()))
   ```

### Exemplo de Saída
```
Conectando...
Conectando...
Conectado!
Configurações de rede: ('192.168.0.100', '255.255.255.0', '192.168.0.1', '8.8.8.8')
```

## Configuração
- **SSID:** Substitua `'rede'` pelo SSID da sua rede Wi-Fi.
- **Senha:** Substitua `'senha1234'` pela senha da sua rede Wi-Fi.

## Contribuição
Se desejar contribuir com melhorias, por favor, crie um fork deste repositório, faça as alterações e envie um pull request.

---

Sinta-se à vontade para adaptar este README conforme necessário para atender às suas necessidades específicas.
