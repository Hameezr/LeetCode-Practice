import React from 'react';

function Rand5() {
  const randomNumber = Math.floor(Math.random() * 5) + 1;
  return randomNumber;
}

const Rand7 = () => {
    const [randomNumber, setRandomNumber] = React.useState(null);

  const rand7 = () => {
    let num = 5 * Rand5() + Rand5();
    while (num > 21) {
      num = 5 * Rand5() + Rand5();
    }
    setRandomNumber(num % 7 + 1);
  };

  return (
    <div>
      <button onClick={() => console.log(rand7())}>Generate a random number</button>
      {randomNumber && <h4>Random Number: {randomNumber}</h4>}
    </div>
  );
};

export default Rand7;
