async function sendConsent(shouldSave, name) {
  try {
    const backendUrl = CONFIG.BACKEND_URL;
    const response = await fetch(`${backendUrl}/locations/save`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ shouldSave, name })
    });
    const data = await response.json();
    console.log('Backend response:', data);
    return data;
  } catch (err) {
    console.error('Error sending consent:', err);
  }
}

function showConsentPopup() {
  const template = document.getElementById('consent-popup-template');
  const popupFragment = template.content.cloneNode(true);
  document.body.appendChild(popupFragment);

  const popupEl = document.body.querySelector('#popup');
  const yesBtn = popupEl.querySelector('#yes-btn');
  const noBtn = popupEl.querySelector('#no-btn');
  const closeBtn = popupEl.querySelector('#close-btn');
  const nameInput = popupEl.querySelector('#name-input');

  yesBtn.addEventListener('click', async () => {
    const name = nameInput.value.trim() || null;
    await sendConsent(true, name);
    popupEl.remove();
  });

  noBtn.addEventListener('click', async () => {
    await sendConsent(false, null);
    popupEl.remove();
  });

  closeBtn.addEventListener('click', async () => {
    await sendConsent(false, null);
    popupEl.remove();
  });
}
