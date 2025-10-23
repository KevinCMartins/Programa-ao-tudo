function adicionarTarefa() {
    let mensagem = "Tarefa adicionada com sucesso!";

    let inputTarefa = document.getElementById('inputTarefa')
    let tarefa = inputTarefa.value
    document.getElementById("mensagem").textContent = mensagem;

    let listaTarefas = document.getElementById('listaTarefas')
    let novatarefa = document.createElement('li')

    novatarefa.textContent = tarefa

    listaTarefas.appendChild(novatarefa)

    inputTarefa.value = ''
}