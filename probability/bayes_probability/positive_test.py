def positive_test(TP, FP, perc_population):
  '''
  Parameters
  ----------
  TP: {float} true positive
      percentage of tests that were positive
      for the sample of subjects that had the disease
  FP: {float} false positive
      percentage of tests that were positive
      for the control population (disease-free subjects)

  percent_population : {float} percentage of the population that has the 
  disease

  Returns
  -------
  {float} probability of having the disease for a person with a positive 
  test result
  '''
  perc_pop_TP = TP * perc_population
  perc_pop_FP = FP * (1 - perc_population)
  return perc_pop_TP / (perc_pop_TP + perc_pop_FP)