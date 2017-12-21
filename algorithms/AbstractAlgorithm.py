from abc import ABCMeta, abstractmethod
import os, sys
from preprocessing.deprecated.prepare_german import prepare_german
from preprocessing.deprecated.prepare_adult import prepare_adult
from preprocessing.deprecated.prepare_retailer import prepare_retailer
from preprocessing.deprecated.prepare_ricci import prepare_ricci
import numpy as np
import pandas as pd
from preprocessing.deprecated.black_box_auditing import *
from data.german.load_german_data import *
from data.adult.load_adult import *
from data.ricci.load_data import *
from metrics.metrics import *

class AbstractAlgorithm(object):
  __metaclass__ = ABCMeta

  def __init__(self, data, params): #, prepare, classify):
    """ data: str for which data set to use
	params: dict with param name as key and val as val (ex: {"eta": 30})
    """
    
    self.data = data
    self.params = params
#    self.prepare = None
#    self.classify = None

    if data == "adult":
      self.prepare = prepare_adult
      self.name = "sex_adult"
      self.filename = "feldmen_cleaned_sex_adult_nb_0"
      self.classify = classify_adult
    '''
    if data == "compas":
      self.prepare = prepare_compas
      self.name = "propublica"
      self.filename = "propublica_race_nb_0"
      self.classify = classify_compas
    '''
    if data == "german":
      self.prepare = prepare_german
      self.name = "german"
      self.filename = "german_sex_nb_0"
      self.classify = classify_german

    if data == "small-retailer":
      self.prepare = prepare_small_retailer
      self.name = "small-retailer"
      self.filename = "retailer_cleaned_race_nb_0"
      self.classify = classify_retailer

    if data == "retailer":
      self.prepare = prepare_retailer
      self.name = "retailer"
      self.filename = "retailer_cleaned_race_nb_0"
      self.classify = classify_retailer

    if data == "ricci":
      self.prepare = prepare_ricci
      self.name = "ricci"
      self.filename = "ricci_cleaned_race_nb_0"
      self.classify = classify_ricci

    self.x_train, self.y_train, self.x_control_train, self.x_test, self.y_test, self.x_control_test, self.sensitive_attr = self.prepare()

  @abstractmethod
  def run(self):
   """ runs algorithm and returns inputs for Metrics """
   pass
  
