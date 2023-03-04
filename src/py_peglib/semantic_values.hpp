#pragma once

#include <boost/python.hpp>

#include <peglib.h>

namespace py_peglib {

    class semantic_values {
        const ::peg::SemanticValues& sv;
        
    public:

        semantic_values(const ::peg::SemanticValues& sv);

        virtual ~semantic_values() = default;
        
        long size() const;

        long choice() const;
        
        boost::python::object at(const long& index);

        const std::string to_string() const;
    };

}
