from pyscript import document, window
from pyscript import when
from appUtils import createTodoElement

@when("click", "#createTodoBtn")
def click_handler(event):
    print("Add todo button is clicked")
    todoTxtInpEl = document.querySelector("#todoInp")
    todoTxt = todoTxtInpEl.value.strip()
    if todoTxt == "":
        window.alert("Todo text is empty...")
        return
    todoRow = createTodoElement(todoTxt)
    todosTable = document.querySelector("#todosTable")
    todosTable.appendChild(todoRow)
    todoTxtInpEl.value = ""