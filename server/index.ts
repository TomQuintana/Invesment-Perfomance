import express from 'express';

export const app = express();

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
})
