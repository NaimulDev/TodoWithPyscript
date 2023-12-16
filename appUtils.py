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
    deleteBtn.style.padding = "10px"
    deleteBtn.style.backgroundColor = "#ff7fb0"

    todoRowEl = document.createElement("tr")
    todoLabelCell = document.createElement("td")
    todoDelBtnCell = document.createElement("td")
    todoLabelCell.appendChild(label)
    todoDelBtnCell.appendChild(deleteBtn)
    todoRowEl.appendChild(todoLabelCell)
    todoRowEl.appendChild(todoDelBtnCell)

    todoRowEl.style.backgroundColor = "#f2f2f2"
    todoRowEl.style.padding = "10px"
    todoRowEl.style.border = "1px solid #ddd"
    todoRowEl.style.boxShadow = "0 20px 50px rgba(240, 46, 170, 0.7)"


    def del_task(evt):
        print("Deleting task...")
        rowEl = evt.target.parentNode.parentNode
        tableEl = rowEl.parentNode
        tableEl.removeChild(rowEl)
    
    deleteBtn.onclick = del_task
    
    return todoRowEl