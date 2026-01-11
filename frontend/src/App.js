import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/expenses/api/expenses/')
      .then(response => response.json())
      .then(data => {
        setExpenses(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching expenses:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Expense Tracker</h1>
      </header>
      <main>
        <h2>Expenses</h2>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <ul>
            {expenses.map(expense => (
              <li key={expense.expense_id}>
                {expense.description} - ${expense.amount} ({expense.category}) - {expense.expense_date}
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
}

export default App;
