document.querySelector('#consulta').addEventListener('submit', async (event) => {
  event.preventDefault();
  const title = document.querySelector('#titulo');
  const state = document.querySelector('#estado');
  const output = document.querySelector('#resposta');
  title.textContent = 'Consultando…'; state.textContent = ''; output.textContent = '';
  try {
    const id = document.querySelector('#recurso').value.trim();
    const response = await fetch('/api/v1/recursos/' + encodeURIComponent(id));
    const payload = await response.json();
    output.textContent = JSON.stringify(payload, null, 2);
    if (!response.ok) throw new Error('Consulta recusada: HTTP ' + response.status);
    for (const field of ['id', 'nome', 'status']) {
      if (typeof payload[field] !== 'string' || !payload[field]) throw new Error('Resposta sem campo obrigatório: ' + field);
    }
    title.textContent = payload.nome;
    state.textContent = payload.id + ' · ' + payload.status;
  } catch (error) {
    title.textContent = 'Não foi possível concluir a consulta'; state.textContent = error.message;
  }
});
