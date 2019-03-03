let backendHost;

const hostname = window && window.location && window.location.hostname;

if (hostname === 'ec2-18-235-225-4.compute-1.amazonaws.com') {
  backendHost = 'http://ec2-18-235-225-4.compute-1.amazonaws.com';
} else {
  backendHost = 'http://127.0.0.1:5000';
}

window.API_ROOT = `${backendHost}/api`;