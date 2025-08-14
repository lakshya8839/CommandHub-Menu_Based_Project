# Full_stack_tasks.py
import streamlit as st
import json

st.set_page_config(page_title="All Web Tasks — Streamlit", layout="wide")

st.sidebar.header("Backend (optional)")
backend_url = st.sidebar.text_input(
    "Backend base URL (leave empty to use built-in mock handlers)",
    value="",
    placeholder="http://localhost:3000"
)
st.sidebar.markdown(
    """
**Notes**
- If you run a real backend (Node/Flask) implement endpoints: `/api/chat`, `/api/image`, `/api/search`, `/upload_instagram`.
- If left empty, the page uses built-in mock responses so UI features work locally without a server.
- For camera/mic access: open `http://localhost:8501` (localhost works fine for browser permissions).
"""
)

# JSON-encode backend_url so it's safe to inject into JS
backend_js_string = json.dumps(backend_url)

# HTML template (no f-string). Use a placeholder __BACKEND_URL_PLACEHOLDER__ to inject backend URL safely.
html_template = '''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>All Web Tasks — One File</title>
<style>
  body{font-family:Inter,system-ui,Segoe UI,Roboto,Arial;line-height:1.45;background:#0f172a;color:#e6eef8;padding:18px;}
  h1,h2{color:#fff}
  .card{background:#0b1220;border:1px solid rgba(255,255,255,0.04);padding:14px;border-radius:10px;margin:10px 0}
  button{padding:8px 12px;border-radius:8px;border:0;background:#7c3aed;color:white;cursor:pointer}
  video,canvas{border-radius:8px;display:block;margin:8px 0;max-width:100%}
  .row{display:flex;gap:12px;flex-wrap:wrap}
  input,textarea,select{padding:8px;border-radius:6px;border:1px solid rgba(255,255,255,0.06);background:#071023;color:#e6eef8}
  #log{white-space:pre-wrap;background:#071127;padding:8px;border-radius:8px;max-height:220px;overflow:auto}
  #box{width:150px;height:100px;background:#1f2937;color:#fff;position:relative;cursor:grab;display:flex;align-items:center;justify-content:center;border-radius:8px}
  .small{font-size:13px;color:#a8b3c7}
  .section-grid{display:grid;grid-template-columns:1fr;gap:12px}
  @media(min-width:900px){ .section-grid{grid-template-columns:repeat(2,1fr)} }
</style>
</head>
<body>

<h1>All Web Tasks — One File</h1>
<p class="small">Open on localhost/HTTPS. Server-required features call placeholder endpoints — the page will use built-in mock handlers if you did not provide a backend URL in Streamlit sidebar.</p>

<!-- ===== Mic -> Speech-to-text (Task 1) ===== -->
<div class="card">
  <h2>Mic → Speech-to-Text (Web Speech API)</h2>
  <div class="row">
    <button id="startStt">Start Listening</button>
    <button id="stopStt">Stop</button>
    <select id="langStt"><option value="en-US">English (en-US)</option><option value="hi-IN">Hindi (hi-IN)</option></select>
  </div>
  <div id="sttText" class="small" style="margin-top:8px">Transcript will appear here...</div>
</div>

<!-- ===== Camera preview + Snap photo (Task 2 + 3) ===== -->
<div class="card">
  <h2>Camera Preview & Snap Photo</h2>
  <video id="camPreview" autoplay playsinline width="480"></video>
  <div class="row">
    <button id="startCam">Start Camera</button>
    <button id="snapPhoto">Snap Photo</button>
    <button id="stopCam">Stop Camera</button>
  </div>
  <canvas id="photoCanvas" width="480" height="360"></canvas>
  <div class="small">Saved image as data URL (open console to see full dataURL). You can upload it to backend (mocked here).</div>
</div>

<!-- ===== Live stream explanation (Task 3 remote) ===== -->
<div class="card">
  <h2>Live Stream (local) & WebRTC hint</h2>
  <p class="small">The video above is the local live stream. To broadcast to remote viewers use WebRTC + signaling server, or stream to an RTMP server via a media server (requires server-side components).</p>
</div>

<!-- ===== Record video (Task 4) ===== -->
<div class="card">
  <h2>Record Video & Auto-upload (to server) — MediaRecorder</h2>
  <div class="row">
    <button id="startRec">Start Recording</button>
    <button id="stopRec">Stop Recording</button>
    <button id="uploadRec">Upload to Server (Instagram flow)</button>
  </div>
  <video id="recPreview" controls width="360"></video>
  <div class="small">Upload endpoint: <code>/upload_instagram</code> — mocked locally unless you provided a backend.</div>
</div>

<!-- ===== Search name in Google & collect links (Task 5) ===== -->
<div class="card">
  <h2>Search Name & Collect Links (needs backend/API)</h2>
  <div class="row">
    <input id="searchName" placeholder="Type name to search (e.g., 'Arjun Prajapat')" />
    <button id="doSearch">Search</button>
  </div>
  <div id="searchResults" class="small" style="margin-top:8px">Results will appear here (mocked locally if no backend).</div>
  <div class="small">Tip: use Google Custom Search JSON API or your own scraper backend; client scraping of Google is blocked/CORS-protected.</div>
</div>

<!-- ===== Google Apps Script example (Task 6) ===== -->
<div class="card">
  <h2>Google Apps Script Example</h2>
  <p class="small">This GAS script copies Gmail attachments to Drive and logs in a Sheet. Paste into <code>script.google.com</code>.</p>
  <textarea id="gasCode" style="width:100%;height:130px;">
function archiveGmailAttachments() {
  const label = GmailApp.getUserLabelByName('ArchiveToDrive');
  const threads = label.getThreads(0, 10);
  const folder = DriveApp.getFolderById('YOUR_DRIVE_FOLDER_ID');
  threads.forEach(t => {
    const msgs = t.getMessages();
    msgs.forEach(m => {
      m.getAttachments().forEach(att => {
        folder.createFile(att.copyBlob());
      });
    });
    t.removeLabel(label);
  });
}
  </textarea>
  <div class="small">Change label & folder ID; set a time-driven trigger to run regularly.</div>
</div>

<!-- ===== Drag & Drop Div (Task 7) ===== -->
<div class="card">
  <h2>Drag & Drop DIV</h2>
  <div id="box">Drag me</div>
  <div class="small">Click and drag the box above.</div>
</div>

<!-- ===== ChatGPT Integration (Task 8) ===== -->
<div class="card">
  <h2>ChatGPT Integration via Backend Proxy</h2>
  <textarea id="chatPrompt" placeholder="Type prompt to send to ChatGPT" style="width:100%;height:70px"></textarea>
  <div class="row" style="margin-top:8px">
    <button id="sendChat">Send to ChatGPT</button>
    <button id="clearLog">Clear Log</button>
  </div>
  <div id="log" class="small"></div>
  <div class="small">Client calls <code>/api/chat</code>. If you provided a backend URL in the Streamlit sidebar the page will forward requests there; otherwise a mock reply will be generated locally.</div>
</div>

<!-- ===== Mic-to-ChatGPT (Task 9) ===== -->
<div class="card">
  <h2>Mic → Prompt → ChatGPT</h2>
  <div class="row">
    <button id="startSpeak">Start & Send Spoken Prompt</button>
    <button id="stopSpeak">Stop</button>
  </div>
  <div class="small" id="spokenStatus">Press start, speak, and it will send the final transcript to ChatGPT via /api/chat (mocked if no backend).</div>
</div>

<!-- ===== Image generation (Task 10) ===== -->
<div class="card">
  <h2>Generate Image (via backend API)</h2>
  <input id="imgPrompt" placeholder="Image prompt (e.g., 'cinematic portrait of a coder')" style="width:70%" />
  <button id="genImage">Generate</button>
  <div id="generatedImage" style="margin-top:8px"></div>
  <div class="small">Client calls <code>/api/image</code>, which is mocked locally unless you provided a backend.</div>
</div>

<script>
/* ============================
   Backend helper + mocks
   ============================ */
window.BACKEND_BASE = __BACKEND_URL_PLACEHOLDER__;

async function apiFetch(path, options = {}) {
  // If user provided a real backend URL, forward the request there.
  if (window.BACKEND_BASE && window.BACKEND_BASE.length > 0) {
    // Ensure path has leading slash and trim trailing slash from base
    const base = window.BACKEND_BASE.replace(/\/$/, '');
    const url = (path.startsWith('http') ? path : (base + path));
    return fetch(url, options);
  }

  // NO BACKEND: use local mocks for the endpoints used by the page.
  // Return object with .json() method to mimic Fetch Response.
  const respond = (obj) => {
    return {
      ok: true,
      status: 200,
      json: async () => obj
    };
  };

  // Helper to get parsed JSON body if present
  const getJsonBody = () => {
    if (!options || !options.body) return {};
    try {
      if (typeof options.body === 'string') return JSON.parse(options.body);
      // If it's an object already (rare), return it
      return options.body;
    } catch (e) {
      return {};
    }
  };

  // Handle endpoints
  if (path.endsWith('/api/chat')) {
    const body = getJsonBody();
    const prompt = (body && body.prompt) ? body.prompt : "(no prompt)";
    const reply = `Mock ChatGPT reply — you sent: "${prompt}"`;
    return respond({ reply });
  }

  if (path.endsWith('/api/image')) {
    // create a canvas-based image with prompt text and return base64
    const body = getJsonBody();
    const prompt = (body && body.prompt) ? body.prompt : "mock image";
    const c = document.createElement('canvas');
    const W = 512, H = 360;
    c.width = W; c.height = H;
    const ctx = c.getContext('2d');
    // background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0,0,W,H);
    // title
    ctx.fillStyle = '#e6eef8';
    ctx.font = '20px Arial';
    const lines = [];
    const wrap = (s, maxChars) => {
      while (s.length > maxChars) {
        lines.push(s.slice(0, maxChars));
        s = s.slice(maxChars);
      }
      lines.push(s);
    };
    wrap(prompt.slice(0,500), 36);
    let y = 40;
    for (let i=0;i<lines.length;i++) {
      ctx.fillText(lines[i], 12, y);
      y += 26;
      if (y > H-20) break;
    }
    // small footer
    ctx.fillStyle = '#a8b3c7';
    ctx.font = '12px Arial';
    ctx.fillText('Generated (mock) image for: ' + prompt.slice(0,40), 12, H-12);
    const dataUrl = c.toDataURL('image/png');
    const b64 = dataUrl.split(',')[1];
    return respond({ b64 });
  }

  if (path.endsWith('/api/search')) {
    const body = getJsonBody();
    const q = (body && body.q) ? body.q : '';
    // Return mocked list of links
    const items = [];
    for (let i=1;i<=5;i++) {
      items.push({
        title: `Mock result ${i} for "${q}"`,
        link: `https://example.com/search?q=${encodeURIComponent(q)}&r=${i}`,
        snippet: `This is a mocked search snippet for result ${i} matching "${q}".`
      });
    }
    return respond({ query: q, results: items });
  }

  if (path.endsWith('/upload_instagram')) {
    // options.body often is a FormData in the page. We can read file size if present.
    if (options && options.body && typeof options.body.get === 'function') {
      const file = options.body.get('file');
      if (file && file.size) {
        return respond({ status: 'received', size: file.size });
      }
    }
    return respond({ status: 'no-file' });
  }

  // default fallback
  return respond({ error: 'No mock implementation for ' + path });
}

/* ============================
   Utilities & feature glue (original logic)
   ============================ */
const logEl = document.getElementById('log');
function log(s){ if(logEl) { logEl.textContent += s + "\\n\\n"; logEl.scrollTop = logEl.scrollHeight; } }

/* ===== Task 1: Mic -> Speech-to-Text (Web Speech API) ===== */
let recognition, recognizing=false;
document.getElementById('startStt').onclick = ()=>{
  const lang = document.getElementById('langStt').value;
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SpeechRecognition){ alert('SpeechRecognition not supported in this browser (use Chrome).'); return; }
  recognition = new SpeechRecognition();
  recognition.lang = lang;
  recognition.interimResults = true;
  recognition.onresult = e => {
    const text = Array.from(e.results).map(r => r[0].transcript).join('');
    document.getElementById('sttText').textContent = text;
  };
  recognition.onend = ()=> { recognizing=false; document.getElementById('sttText').textContent += " (ended)"; };
  recognition.start(); recognizing=true;
};
document.getElementById('stopStt').onclick = ()=>{
  if(recognition && recognizing) recognition.stop();
};

/* ===== Task 2/3: Camera preview & Snap ===== */
let localStream = null;
const camPreview = document.getElementById('camPreview');
document.getElementById('startCam').onclick = async ()=>{
  try{
    localStream = await navigator.mediaDevices.getUserMedia({video:true,audio:false});
    camPreview.srcObject = localStream;
  }catch(err){ alert('Camera permission denied or no camera: '+err.message); }
};
document.getElementById('stopCam').onclick = ()=>{
  if(localStream) localStream.getTracks().forEach(t=>t.stop());
  camPreview.srcObject = null;
};
document.getElementById('snapPhoto').onclick = ()=>{
  const c = document.getElementById('photoCanvas');
  const ctx = c.getContext('2d');
  try{
    ctx.drawImage(camPreview, 0, 0, c.width, c.height);
    const dataUrl = c.toDataURL('image/png');
    console.log('photo dataURL (truncated):', dataUrl.slice(0,120)+'...');
    alert('Photo snapped — check console for dataURL (or send to backend).');
  }catch(e){
    alert('Unable to snap photo. Make sure camera is running and allowed.');
  }
};

/* ===== Task 4: Record video using MediaRecorder ===== */
let recorder, recordedBlobs;
const recPreview = document.getElementById('recPreview');
document.getElementById('startRec').onclick = async ()=>{
  recordedBlobs = [];
  if(!localStream){
    try{ localStream = await navigator.mediaDevices.getUserMedia({video:true,audio:true}); camPreview.srcObject = localStream; }
    catch(err){ alert('Need camera + mic to record: '+err.message); return; }
  }
  try{
    recorder = new MediaRecorder(localStream, {mimeType:'video/webm;codecs=vp9,opus'});
  }catch(e){
    recorder = new MediaRecorder(localStream);
  }
  recorder.ondataavailable = e=> { if(e.data && e.data.size) recordedBlobs.push(e.data); };
  recorder.onstop = ()=>{
    const superBuffer = new Blob(recordedBlobs, {type:'video/webm'});
    recPreview.src = URL.createObjectURL(superBuffer);
  };
  recorder.start(1000);
  log('Recording started.');
};
document.getElementById('stopRec').onclick = ()=>{
  if(recorder && recorder.state !== 'inactive'){ recorder.stop(); log('Recording stopped.'); }
};
/* Upload recorded video to server endpoint (placeholder) */
document.getElementById('uploadRec').onclick = async ()=>{
  if(!recordedBlobs || recordedBlobs.length===0){ alert('No recording available.'); return; }
  const blob = new Blob(recordedBlobs, {type:'video/webm'});
  const fd = new FormData();
  fd.append('file', blob, 'recording.webm');
  log('Uploading recording to /upload_instagram (mock / real based on sidebar)...');
  try{
    const res = await apiFetch('/upload_instagram', {method:'POST', body: fd});
    const j = await res.json();
    log('Server response: ' + JSON.stringify(j));
    alert('Upload completed (see log).');
  }catch(err){ log('Upload failed: '+err.message); alert('Upload failed: check backend.'); }
};

/* ===== Task 5: Search name & collect links (calls backend /api/search) ===== */
document.getElementById('doSearch').onclick = async ()=>{
  const name = document.getElementById('searchName').value.trim();
  if(!name) return alert('Type a name first.');
  document.getElementById('searchResults').textContent = 'Searching...';
  try{
    const res = await apiFetch('/api/search', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({q:name})});
    const j = await res.json();
    document.getElementById('searchResults').textContent = JSON.stringify(j,null,2);
  }catch(err){
    document.getElementById('searchResults').textContent = 'Search failed (no backend). See sample backend in file comments.';
  }
};

/* ===== Task 7: Drag & Drop DIV ===== */
const box = document.getElementById('box');
let dragging=false, ox=0, oy=0;
box.addEventListener('mousedown', e=>{
  dragging=true; ox = e.clientX - box.offsetLeft; oy = e.clientY - box.offsetTop; box.style.cursor='grabbing';
});
document.addEventListener('mousemove', e=>{
  if(!dragging) return;
  box.style.left = (e.clientX - ox) + 'px';
  box.style.top = (e.clientY - oy) + 'px';
});
document.addEventListener('mouseup', ()=>{ dragging=false; box.style.cursor='grab'; });

/* ===== Task 8: ChatGPT Integration via backend ===== */
document.getElementById('sendChat').onclick = async ()=>{
  const prompt = document.getElementById('chatPrompt').value.trim();
  if(!prompt) return alert('Type a prompt first.');
  log('Sending prompt to /api/chat ...');
  try{
    const res = await apiFetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({prompt})});
    const j = await res.json();
    if(j.error) log('Error: '+JSON.stringify(j.error));
    else log('ChatGPT response:\\n' + (j.reply || JSON.stringify(j,null,2)));
  }catch(err){ log('Chat request failed: '+err.message); }
};
document.getElementById('clearLog').onclick = ()=> { if(logEl) logEl.textContent = ''; };

/* ===== Task 9: Mic input -> ChatGPT (combine STT + /api/chat) ===== */
let interimRecognizer;
document.getElementById('startSpeak').onclick = async ()=>{
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if(!SpeechRecognition){ alert('SpeechRecognition not supported.'); return; }
  interimRecognizer = new SpeechRecognition();
  interimRecognizer.lang = 'en-US';
  interimRecognizer.interimResults = false;
  interimRecognizer.onresult = async e=>{
    const text = Array.from(e.results).map(r=>r[0].transcript).join('');
    document.getElementById('spokenStatus').textContent = 'Heard: ' + text;
    // send to backend ChatGPT
    try{
      const res = await apiFetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({prompt:text})});
      const j = await res.json();
      log('Spoken prompt -> ChatGPT reply:\\n' + (j.reply || JSON.stringify(j)));
    }catch(err){ log('Failed to send spoken prompt: '+err.message); }
  };
  interimRecognizer.onend = ()=> document.getElementById('spokenStatus').textContent += ' (ended)';
  interimRecognizer.start();
};
document.getElementById('stopSpeak').onclick = ()=> { if(interimRecognizer) interimRecognizer.stop(); };

/* ===== Task 10: Generate Image via backend (/api/image) ===== */
document.getElementById('genImage').onclick = async ()=>{
  const prompt = document.getElementById('imgPrompt').value.trim();
  if(!prompt) return alert('Type image prompt');
  document.getElementById('generatedImage').textContent = 'Generating...';
  try{
    const res = await apiFetch('/api/image', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({prompt})});
    const j = await res.json();
    if(j.url){
      document.getElementById('generatedImage').innerHTML = '<img src="'+j.url+'" style="max-width:100%;border-radius:8px"/>';
    }else if(j.b64){
      document.getElementById('generatedImage').innerHTML = '<img src="data:image/png;base64,'+j.b64+'" style="max-width:100%;border-radius:8px"/>';
    }else document.getElementById('generatedImage').textContent = JSON.stringify(j);
  }catch(err){ document.getElementById('generatedImage').textContent = 'Failed: '+err.message; }
};

/* ===== End of client code ===== */
</script>

<!--
================================================================
SAMPLE BACKEND (Node/Express) - minimal examples for endpoints used above.
Save as server.js, run: node server.js after npm install express node-fetch multer
(These are minimal; secure them, use env vars, and add error handling.)
================================================================

... (backend sample unchanged, present for reference in comments) ...

-->
</body>
</html>
'''

# Inject backend_js_string safely into the template
html_content = html_template.replace("__BACKEND_URL_PLACEHOLDER__", backend_js_string)

# Render the HTML inside Streamlit
st.components.v1.html(html_content, height=1200, scrolling=True)
