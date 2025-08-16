# Icon Hider - Um atalho para um ecrã limpo!

![GIF de um ecrã a ficar limpo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWI5eWdvZzViZmg3YTF2OTdta2Jjd3Z5ODNrdW94cHJkZTlzNmw4NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Yz88Wd7UuGUIlCUaRp/giphy.gif)

Cansado de clicar com o botão direito para "Ocultar ícones da área de trabalho"? Ou simplesmente tem preguiça de fazer sempre que precisa da Área de Trabalho limpa para uma apresentação? Eu também. Por isso, criei esta pequena ferramenta em Python para resolver o problema com uma única tecla.

## Para que serve isto?

É simples: você aperta **F12** e todos os ícones da sua área de trabalho somem. Aperte **F12** de novo e eles voltam.

## Como eu uso? (A versão fácil)

1.  Vá à aba de **[Releases](https://github.com/Mentus99/IconHiderApp/releases)** e baixe o `IconHider.exe`.
2.  Dê dois cliques para executar. Não vai aparecer nenhuma janela, é assim mesmo.
3.  Teste a tecla **F12**!
4.  **Para fechar a app:** Como não tem ícone, precisa de abrir o Gerenciador de Tarefas e procurar por `IconHider.exe` e clicar em "Finalizar tarefa".

## E se eu quiser mexer no código?

Se você também está aprendendo python como eu e quer mexer no código, o caminho é este:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Mentus99/IconHiderApp.git](https://github.com/Mentus99/IconHiderApp.git)
    ```
2.  **Instale o que precisa:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute o script:**
    ```bash
    python IconHider.py
    ```

### Quer criar o seu próprio .exe?

Eu usei o PyInstaller. O comando é este aqui:
```bash
python -m PyInstaller --onefile --windowed --name IconHider IconHider.py
## Licença

Este projeto é de código aberto e está licenciado sob a **[Licença MIT](LICENSE)**. Basicamente, você pode fazer o que quiser com o código, desde que mantenha os créditos.

## Contato

Quer trocar uma ideia, sugerir algo ou só se conectar? Me encontre aqui:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabriel-mendes2499/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gabriel.mendes.rodrigues@gmail.com)
