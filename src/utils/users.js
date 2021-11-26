export function userStorageFormat() {
  let settings = localStorage.getItem('user');
  if (settings) return JSON.parse(settings);
  else localStorage.setItem('user', '{}');

  return {};
}
export function userCheck() {
  const userData = localStorage.getItem('user');

  if (userData === '{}' || userData === undefined || userData === null)
    return false;
  else return true;
}

export function lineLogout() {
  localStorage.setItem('user', '{}');
  window.location.reload();
}

export async function createGame(game) {
  const url = process.env.VUE_APP_API_URL;
  const user = userStorageFormat();

  await fetch(`${url}/users/${user.uid}/games/`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      score: game.score,
      level: game.level,
    }),
  });
}

async function styleStorageFormat(style) {
  const defaultStyle = {
    color: '#000000',
    size: '18px',
    duration: 10,
    level: 0,
  };

  if (style) {
    localStorage.setItem('style', JSON.stringify(style));
    return style;
  }
  else {
    const url = process.env.VUE_APP_API_URL,
      user = userStorageFormat();
    await fetch(`${url}/users/${user.uid}/style/`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(defaultStyle),
    });

    localStorage.setItem('style', JSON.stringify(defaultStyle));
  }

  return defaultStyle;
}

export async function getStyle() {
  const url = process.env.VUE_APP_API_URL;
  const user = userStorageFormat();

  return await fetch(`${url}/users/${user.uid}/games/`);
}

export async function setStyle() {
  const url = process.env.VUE_APP_API_URL,
    user = userStorageFormat();
  const style = await fetch(`${url}/users/${user.uid}/style/`);
  return styleStorageFormat(await style.json());
}

export async function createStyle(style) {
  const url = process.env.VUE_APP_API_URL;
  const user = userStorageFormat();

  await fetch(`${url}/users/${user.uid}/styles/`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      size: style.size,
      color: style.color,
    }),
  });
}
