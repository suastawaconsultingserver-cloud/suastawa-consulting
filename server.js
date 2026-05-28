const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ status: 'Suastawa Consulting API berjalan!' });
});

app.listen(PORT, () => {
  console.log(`Server berjalan di port ${PORT}`);
});
