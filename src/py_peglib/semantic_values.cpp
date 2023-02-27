#include "semantic_values.hpp"

namespace py_peglib {

    semantic_values::semantic_values(const ::peg::SemanticValues& sv)
        : sv(sv)
    {}

    long semantic_values::size() const
    {
        return sv.size();
    }

    const std::string semantic_values::to_string() const
    {
        return sv.token_to_string();
    }
}