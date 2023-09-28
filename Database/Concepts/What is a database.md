## How to create a database-like file through javascript

- Create a file called, database.mjs, with the following content:
```javascript
export var users = [
{ "Name": "..."},
...
]
```
- Then using the Node [[REPL]] the following command:
```javascript
db = await import('./files/users.mjs')
```
- Then would be possible to use ```console.table(db.users)``` to display a table through the json file.
### Note:

*Node.js* original module system is [[CommonJs]] which uses **require** and **module.exports**.

e.g:

```javascript
module.exports = class Square { constructor(a) { this.a = a }}

const circle = require('./circle.js');
```

[[ECMAScript module system]] which uses **import** and **export** has become standard and node.js has added support for it.

e.g:

```javascript
// addTwo.mjs
function addTwo(num) {
  return num + 2;
}

export { addTwo };
```

```javascript
// app.mjs
import { addTwo } from './addTwo.mjs';

// Prints: 6
console.log(addTwo(4));
```

Note: The export default syntax **allows you to export a single value from a module as the default export**. When another module imports the module that uses export default , the imported value will be whatever value was exported as the default. You can only have one default export per module.

So Node.js will treat <mark>.cjs</mark> files as CommonJS modules and <mark>.mjs</mark> files as ECMAScript modules and it will treat <mark>.js</mark> files as whatever the default module system for the project is, which is CommonJS unless package.json says:

```javascript
"type": "module"
```

### "Operations":

***INSERT***
```javascript
db.users.push({})
```

***SELECT***
```javascript
let result = db.users.filter(user => user.name === 'Name')

console.table(result) 
```

### Javascript statment methods

***SELECT***
```javascript
export const select = (columns, result) => {
    switch(columns) {
        case '*':
            columns = Object.keys(result[0])
            break;
        case 'count':
            return result.length
        default:
            columns = columns.split(',')
    }
    if (result === undefined) return []
    return result.map(row => columns.map((column) => {
        if (row[column] === undefined) {
            return null
        } else {
            return row[column]
        }
    }).reduce((a, v, i) => ({...a, [columns[i]]: v}), {}))
}
```
- [[Object.keys()]] => returns an array of a given object's own enumerable propeties names, like ```for ... in```.
- [[Array.prototype.reduce]]

****FROM***
```javascript
export const from = (table, conditions) => {
    if (conditions === undefined) {
        if(database[table]) {
            return database[table]
        }
        throw new Error('Table or view not exists');
    } else {
        return eval(`database[table].filter((${table}) => {
            return ${conditions.where}
        })`)
    }
}
```
- [[eval()]]

***ORDER BY***
```javascript
export const orderBy = (column, order, result) => {
    return result.sort((a, b) => {
        let compare = 0
        if(a[column] < b[column]) {
            compare = -1
        } else if (a[column] > b[column]) {
            compare = 1
        }
        return (order === 'asc' ? compare : -compare)
    })
}
```

**INSERT**
```javascript
export const insert = (table, values) => {
    const id = from(table).length + 1
    from(table).push({
        ...values,
        id
    })
    return id
}
```

***DELETE***
```javascript
export const deleteFrom = (table, conditions) => {
    let counter = 0
    from(table, conditions).forEach(row => {
        counter ++
        from(table).pop(row)
    })
    return counter
}  
```

#### References:
1. https://youtu.be/_7nISfpofec?si=KHKDknRlVwoZGFzZ

#database
