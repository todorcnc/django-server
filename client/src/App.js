import React, { useEffect, useState } from 'react';
import './App.css';
import Button from '@mui/material/Button';

function App() {
  let websocket;
  const [retryCount, setRetryCount] = useState(0);
  const MAX_RETRIES = 500;

  useEffect(() => {
    connectToWebSocket();

    // Clean up the websocket connection and timeouts when the component unmounts
    return () => {
      if (websocket) {
        websocket.close();
      }
      // Clear all pending timeouts
      const maxId = setTimeout(() => {});
      for (let i = 0; i < maxId; i++) {
        clearTimeout(i);
      }
    };
  }, []);

  const connectToWebSocket = () => {
    const username = 'userID';  // Retrieve this from your application's state or props
    websocket = new WebSocket(`ws://localhost:8000/ws/websocket/?username=${username}`);

    websocket.onopen = () => {
      console.log('WebSocket connection opened');
      setRetryCount(0); // Reset retry count on a successful connection
    };

    websocket.onmessage = function (e) {
      let data = JSON.parse(e.data);
      console.log(data.message);
    };

    websocket.onerror = (error) => {
      console.error('WebSocket Error', error);
    };

    websocket.onclose = (event) => {
      if (event.wasClean) {
        console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);
      } else {
        console.warn('Connection died');
        if (retryCount < MAX_RETRIES) {
          setTimeout(() => {
            console.log('Attempting to reconnect...');
            setRetryCount((prevCount) => prevCount + 1);
            connectToWebSocket();
          }, 500); // Retry after half a second
        } else {
          console.log('Max retries reached. Stopping reconnection attempts.');
        }
      }
    };
  };

  const sendMessage = () => {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
      const message = { type: "test", content: "Hello, server!" };
      websocket.send(JSON.stringify(message));
    }
  };

  return (
    <div>
      <h1>Hello Websockets</h1>
      <Button variant="contained" color="primary" onClick={sendMessage}>
        Send Message
      </Button>
    </div>
  );
}

export default App;
