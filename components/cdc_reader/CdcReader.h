//
// Created by Marcel Schmidt on 22.03.26.
//
#pragma once

#ifndef ESPHOME_CDCREADER_H
#define ESPHOME_CDCREADER_H

#include "esphome/core/component.h"
#include <esphome/core/hal.h>

namespace esphome::cdc_reader
{
    class CdcReader: public Component
    {

    public:
        virtual ~CdcReader() = default;
        CdcReader();

        void setup() override;
        void dump_config() override;


    };
}


#endif //ESPHOME_CDCREADER_H
