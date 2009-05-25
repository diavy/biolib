    # value = QtlGenotype::NA if @allowed_na.include?(value)
    # individual(ind).phenotypes[pid] = value

class QtlPhenotypeName

  attr_reader :name

  def initialize name
    @name = name
  end
end

class QtlPhenotypeNames < Array

  NA = '-'

  def set idx, value
    self[idx] = QtlPhenotypeName.new(value)
  end
end

class QtlPhenotype
  attr_reader :value
  def set(nvalue)
    @value = nvalue
  end
end

class QtlPhenotypes < Array

  def set pid, value
    self[pid] = QtlPhenotype.new if !self[pid]
    self[pid].set(value)
  end
end

