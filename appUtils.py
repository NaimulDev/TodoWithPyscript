from pyscript import document

def createTodoElement(todoTxt:str):
    deleteBtn = document.createElement("button")
    label = document.createElement("label")
    label.innerText = todoTxt
    deleteBtn.innerText = "x"
    deleteBtn.style.marginLeft = "1em"
    deleteBtn.style.marginBottom = "0.5em"
    deleteBtn.classList.add("btn")
    deleteBtn.classList.add("btn-danger")

    todoRowEl = document.createElement("tr")
    todoLabelCell = document.createElement("td")
    todoDelBtnCell = document.createElement("td")
    todoLabelCell.appendChild(label)
    todoDelBtnCell.appendChild(deleteBtn)
    todoRowEl.appendChild(todoLabelCell)
    todoRowEl.appendChild(todoDelBtnCell)

    def del_task(evt):
        print("Deleting task...")
        rowEl = evt.target.parentNode.parentNode
        tableEl = rowEl.parentNode
        tableEl.removeChild(rowEl)
    
    deleteBtn.onclick = del_task
    
    return todoRowEl