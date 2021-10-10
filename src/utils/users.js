export function userStorageFormat() {
  let settings = localStorage.getItem('user');
  if (settings) return JSON.parse(settings);
  else localStorage.setItem('user', '{}');

  return {};
}
export function userCheck() {
  const userData = localStorage.getItem('user')
  console.log(userData);
  console.log(typeof userData);
  if (userData === '{}' || userData === undefined || userData === null)
    return false;
  else return true;
}

export function lineLogout() {
  localStorage.setItem('user', '{}');
  window.location.reload()
}
