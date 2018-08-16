import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (
  <DataProvider endpoint="api/dishes/"
                render={data => <Table data={data} />} />
);

const wrapper = document.getElementById("app");
console.log('App.js');

wrapper ? ReactDOM.render(<App />, wrapper) : null;
