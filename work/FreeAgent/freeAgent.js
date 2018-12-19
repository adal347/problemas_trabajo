function contains(myObj, myVal) {
    for (let key in myObj) {
      if (myObj[key] === myVal) {
        return key;
      }
      if (Array.isArray(myObj[key]) || typeof myObj[key] === "object") {
        return contains(myObj[key], myVal);
      }
    }
    return null;
}

// Object.keys(myObj) => ["key1","key2", "key3"];
console.log(contains(
    {
        key1: "wa",
        key2: [10, 4, "pe", { id: 13 }],
        key3: {
            subkey3: [
                "pedro",
                {
                    test: 13,
                    wa: "pe",
                },
            ],
        }
    },
    "pe"
));
