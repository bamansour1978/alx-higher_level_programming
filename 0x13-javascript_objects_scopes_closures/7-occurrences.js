#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, curt) => curt === searchElement ? counter + 1 : counter, 0);
};
