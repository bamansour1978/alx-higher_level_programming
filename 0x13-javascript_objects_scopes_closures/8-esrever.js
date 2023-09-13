#!/usr/bin/node
exports.esrever = (list) => {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
