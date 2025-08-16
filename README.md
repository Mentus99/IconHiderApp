# Icon Hider - Um atalho para um ecrã limpo!

![GIF de um gato a esconder o rosto](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzVqZ254a3k0c2Z0a2NqZzZpY2ZqN3A2b3BqN3A2b3BqN3A2b3BqN3A2b3BqNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKS022G1Iu7SbrG/giphy.gif)

Cansado de ter que clicar com o botão direito do rato para "Ocultar ícones da área de trabalho"? Ou simplesmente tem preguiça de o fazer sempre que precisa de um ecrã limpo para uma apresentação? Eu também. Por isso, criei esta pequena ferramenta em Python para resolver o problema com uma única tecla.

## Para que serve isto?

É simples: você prime **F12** e todos os ícones da sua área de trabalho somem. Prime **F12** de novo e eles voltam. Mágico, não é?

## Como eu uso? (A versão fácil)

1.  Vá à secção de **[Releases](https://github.com/Mentus99/IconHiderApp/releases)** e descarregue o ficheiro `IconHider.exe`.
2.  Dê dois cliques para executar. Não vai aparecer nenhuma janela, é mesmo assim.
3.  Teste a tecla **F12**!
4.  **Para fechar a app:** Como não tem ícone, precisa de abrir o Gestor de Tarefas (`Ctrl + Shift + Esc`), procurar por `IconHider.exe` e clicar em "Finalizar tarefa".

## E se eu quiser mexer no código? (A versão dev)

Se você também está a aprender e quer mexer no código, o caminho é este:

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
