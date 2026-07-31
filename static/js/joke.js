// Fetch a joke from the server endpoint and display it in the page
document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('joke-btn')
  const box = document.getElementById('joke-box')
  const setupEl = document.getElementById('joke-setup')
  const punchEl = document.getElementById('joke-punchline')

  if (!btn) return

  btn.addEventListener('click', async function () {
    btn.disabled = true
    btn.textContent = 'Loading...'
    setupEl.textContent = ''
    punchEl.textContent = ''
    box.style.display = 'none'

    try {
      const res = await fetch('/joke')
      if (!res.ok) throw new Error('Failed to fetch joke')
      const data = await res.json()

      if (data.setup && data.punchline) {
        setupEl.textContent = data.setup
        punchEl.textContent = data.punchline
      } else if (data.joke) {
        setupEl.textContent = data.joke
        punchEl.textContent = ''
      } else if (data.error) {
        setupEl.textContent = 'Error: ' + data.error
      } else {
        setupEl.textContent = 'No joke available right now.'
      }

      box.style.display = 'block'

    } catch (err) {
      setupEl.textContent = 'Error fetching joke. Try again later.'
      box.style.display = 'block'
    } finally {
      btn.disabled = false
      btn.textContent = 'Tell me a joke'
    }
  })
})
