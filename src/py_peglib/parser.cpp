#include "parser.hpp"

#include <iostream>

#include "semantic_values.hpp"

namespace py_peglib {

    parser::parser(const std::string& language)
        : lib_parser(language)
    {}

    void parser::on(const std::string& keyword, boost::python::object lambda)
    {
        lib_parser[keyword.c_str()] = [lambda](const ::peg::SemanticValues &sv) {
            return lambda(semantic_values{sv});
        };
    }

    boost::python::object parser::parse(const std::string& value)
    {
        boost::python::object result;
        lib_parser.parse(value, result);
        return result;
    }
}