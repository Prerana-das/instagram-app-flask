// src/services/api.js

const BASE_URL = ''  // if needed later, you can set it to 'http://localhost:5000' or keep it ''

async function request(method, endpoint, body = null) {
  try {
    const res = await fetch(BASE_URL + endpoint, {
      method,
      headers: {
        'Content-Type': 'application/json'
      },
      ...(body && { body: JSON.stringify(body) })
    })
    
    if (!res.ok) {
      console.log(res)
      throw new Error(`HTTP error! status: ${res.status}`)
    }

    return await res.json()
  } catch (error) {
    console.error(`API ${method} error:`, error)
    return null
  }
}

export function apiGet(endpoint) {
  return request('GET', endpoint)
}

export function apiPost(endpoint, body) {
  return request('POST', endpoint, body)
}

export function apiPut(endpoint, body) {
  return request('PUT', endpoint, body)
}

export function apiDelete(endpoint) {
  return request('DELETE', endpoint)
}
